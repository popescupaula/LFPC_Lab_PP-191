import numpy as np

stack = ['$']
word = str()
maximum = 0
matrix = 0

def analyze(prod, start, nonterminals, terminals, string_to_parse):
    global word
    word = str(string_to_parse)
    
    stack.append((start,0))
    
    print('Initial productions:')
    print_productions(prod)

    print('\nFISRT:')
    first = get_first(prod)
    print_f(first)

    print('\nFOLLOW:')
    follow = get_follow(prod, start)
    print_f(follow)
        
    print('\nParsing table:')
    parsing_table = build_parsing_table(first, follow)
    print_parsing_table(parsing_table, terminals)

    (tree, status) = parse(parsing_table, follow, 1)    
    
    print('\nString:', string_to_parse)
    if(status):    
        x = DisplayTree()
        x.print_tree(tree)
    else:
        print("Parsing failed!")

def get_first(prod):
    first = dict()
    for (key, value) in prod.items():
        first[key] = dict()
        for result in value:
            to_add = list()
            if(result[0] == result[0].lower() or result[0] == '#'):
                to_add.append((result[0], result))
            else:
                to_add = get_first_from_string(result[0], prod)

            if(len(to_add) != 0): 
                for (letter, r) in to_add:
                    first[key][letter] = result
            elif(to_add[0][0] == '#'):
                raise Exception('FAILED to compute FIRST('+key+'). Grammar is left-recursive.')

    return first

def get_first_from_string(c, prod):
    value = prod[c]
    found = list()
    for result in value:
        if(result[0] == result[0].lower() or result[0] == '#'):
            found.append((result[0], result))
        else:
            if(c == result[0]):
                found.append(('#', ''))
                
            new_found = get_first_from_string(result[0], prod)
            for (letter, r) in new_found:
                found.append((letter, r))

    return found

def search_follow(prod, word, i):
    follow = dict()
    for (idx, symbol) in enumerate(word):
        if(symbol == symbol.upper()):
            for result in prod[symbol]:
                if(result != '#'):
                    last_nt = word[-1:]
                    if(last_nt == last_nt.upper() and i!= 0):
                        if(not last_nt in follow.keys()):
                            follow[last_nt] = list()

                        follow[last_nt].append('$')

                    new_word = word[:idx] + result + word[idx+1:]
                    new_prod = dict()
                    for (k, v) in prod.items():
                        new_prod[k] = list()
                        for y in v:
                            if(y != result):
                                new_prod[k].append(y)

                    returned = search_follow(new_prod, new_word, i+1)
                    for (k, v) in returned.items():
                        for y in v:
                            if(not k in follow.keys()):
                                follow[k] = list()

                            if(not y in follow[k]):
                                follow[k].append(y)

    for (idx, symbol) in enumerate(word):
        if(idx+1 < len(word)):
            if(symbol == symbol.upper() and word[idx+1] == word[idx+1].lower()):
                if(not symbol in follow.keys()):
                    follow[symbol] = list()

                if(not word[idx+1] in follow[symbol]):
                    follow[symbol].append(word[idx+1])
    
    return follow
    
def get_follow(prod, start):
    follow = search_follow(prod, start, 0)

    for k in prod.keys():
        if(not k in follow.keys()):
            follow[k] = ['$']
    
    return follow

def print_f(data):
    for x in data:
        print(x, '- ', end='')
        for y in data[x]:
            print(y, end=',')
        print()

def print_parsing_table(table, terminals):
    print(end='    ') 
    for t in terminals:
        print(t, '   ', end='')
    print()
    for x in table.keys():
        print(x, end='   ')
        for y in terminals:
            if y in table[x].keys():
                print(table[x][y], ' '*(5-len(table[x][y])), sep='', end='')
            else:
                print('     ', end='')
        print()

def build_parsing_table(first, follow):
    parsing_table = dict()
    for (key1, terminals) in first.items():
        parsing_table[key1] = dict()
        for (key2, production) in terminals.items():
            if(key2 == '#'):
                for symbol in follow[key1]:
                    parsing_table[key1][symbol] = '#'
            
            parsing_table[key1][key2] = production

    return parsing_table

def parse(parsing_table, follow, i):
    global word
    global stack
    global maximum

    node = Tree()
    if(i>maximum):
        maximum = i

    stack_first = stack[-1:][0][0]
    
    if(stack_first == stack_first.lower()):
        node.data = word[0]
        node.degree = i
        node.ls = stack_first
        del stack[-1:]
        word = word[1:]
        
        return (node, True)

    else:
        rules = parsing_table[stack_first]
        if(word[0] in rules.keys()):
            node.data = stack[-1:][0][0]
            node.degree = i
            node.ls = stack[-1:][0][1]
            deleted = stack[-1:]
            del stack[-1:]

            if rules[word[0]] == '#':
                empty_node = Tree()
                empty_node.data = '#'
                empty_node.degree = i+1
                empty_node.ls = stack[-1:][0][1]

                node.children.append(empty_node)
                return (node, True)

            for (idx, c) in enumerate(reversed(rules[word[0]])):
                stack.append((c, len(rules[word[0]])-idx+1))
            
            # building the tree
            for c in rules[word[0]]:                
                (new_children, state) = parse(parsing_table, follow, i+1)
                if(state):
                    node.children.append(new_children)
                else:
                    return (node, False)
        else:
            return (node, False)

    return (node, True)

def print_productions(joined_productions):
    count = 1
    for (key, value) in joined_productions.items():
        for result in value:
            print(str(count) + '.', key + '->' + result)
            count += 1

class Tree(object):
    def __init__(self):
        self.children = list()
        self.data = None
        self.degree = None
        self.ls = None

class DisplayTree():
    def __init__(self): 
        self.matrix = np.array([[' '] * (3*maximum)] * (8*maximum))
        self.i = 0

    def build_representation(self, node, left, right):
        for (idx, c) in enumerate(node.children):
            if(idx < len(node.children)/2):
                self.build_representation(c, 1, 0)
        
        self.matrix[self.i*2,node.degree*2] = node.data
        self.matrix[self.i*2,node.degree*2-1] = '/'*left + '\\'*right
        self.i += 1

        for (idx, c) in enumerate(node.children):
            if(idx >= len(node.children)/2):
                self.build_representation(c, 0, 1)

    def print_tree(self, tree):
        self.build_representation(tree, 0, 0)
        for x in range(self.matrix.shape[1]):
            for y in range(self.matrix.shape[0]):
                print(self.matrix[y,x], end='')
            print()

if __name__ == "__main__":
    start = 'S'

    prod = {'S':['Ag'], 'A':['abcB'], 'B':['Cd'], 'C': ['e', 'eX'], 'D':['e'], 'X':['#', 'fDX']}
    nonterminals = ['S', 'A', 'B', 'C', 'D', 'X']
    terminals = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    string_to_parse = 'abcefedg'

    analyze(prod, start, nonterminals, terminals, string_to_parse)
