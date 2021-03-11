import pandas as pd

n = 4            #no. of states
t = 3            #no. of paths
nfa = {'0': {'a': ['0', '1'], 'b': [''], 'c': ['']}, '1': {'a': [''], 'b': ['2'], 'c': ['']}, '2': {'a': ['2'], 'b': ['3'], 'c': ['0']}, '3': {'a': [''], 'b': [''], 'c': ['']}}    

nfa_final_state = '3'      #final state           
    
new_states_list = []                          
dfa = {}                                      
keys_list = list(list(nfa.keys())[0])                
path_list = list(nfa[keys_list[0]].keys())   

dfa[keys_list[0]] = {}                        
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])   
    dfa[keys_list[0]][path_list[y]] = var            
    if var not in keys_list:                        
        new_states_list.append(var)                  
        keys_list.append(var)                       

while len(new_states_list) != 0:                     
    dfa[new_states_list[0]] = {}                     
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  
            s = ""
            s = s.join(temp)                         
            if s not in keys_list:                   
                new_states_list.append(s)            
                keys_list.append(s)                  
            dfa[new_states_list[0]][path_list[i]] = s   
        
    new_states_list.remove(new_states_list[0])       

if '' in dfa: del dfa['']
print("\nDFA table representation: ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
