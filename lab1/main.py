from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Dictionary:
    def __init__(self):
        self.dictionary = defaultdict(dict)

    def add_edge(self, header, non_terminal, terminal):
        if header not in self.dictionary:
            self.dictionary[header][non_terminal] = terminal
        elif non_terminal not in self.dictionary[header]:
            self.dictionary[header][non_terminal] = terminal
        else:
            self.dictionary[header][non_terminal] += terminal

    def check_grammar(self, start_node, word):
        result = f"{start_node}"
        current_node = self.dictionary[start_node]

        i = 0
        input_length = len(word)
        while i != input_length:

            flag = False


            for current_non_terminal in current_node.keys():

                if current_node == self.dictionary[current_non_terminal]:
                    result += f" -> {current_non_terminal}"
                    flag = True

                if word[i] == current_node[current_non_terminal]:
                    result += f" -> {current_non_terminal}"
                    flag = True

                    if self.dictionary[current_non_terminal]:
                        current_node = self.dictionary[current_non_terminal]
                    break

            if not flag:
                break

            i += 1

        if result[-1] != "$":
            print("This word is not accepted by FA\n")
        else:
            print(f"This word is accepted by FA\n")



my_graph = Dictionary()

my_file = open("file.txt", "r")
for line in my_file:
    my_graph.add_edge(line[0],line[4],line[3])

my_graph.check_grammar("S", "abcac")
my_graph.check_grammar("S", "cac")
my_graph.check_grammar("S", "aabb")

G = nx.MultiGraph()

G.add_nodes_from(['S', 'A', 'B', '$'])
G.add_edges_from([('S', 'S'), ('S', 'A'), ('A', 'B'), ('B', 'B'), ('B', '$')])

plt.figure()
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

