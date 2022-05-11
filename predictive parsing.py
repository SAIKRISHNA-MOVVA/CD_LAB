# Aim:
#A program to construct a Predictive Parsing Table for the given Grammar.

#LL(1) Parsing:
#Here the 1st L represents that the scanning of the Input will be done from Left to Right manner and the second L shows that in this parsing technique we are going to use Left most Derivation Tree. And finally, the 1 represents the number of look-ahead, which means how many symbols are you going to see when you want to make a decision.

 #Algorithm to construct LL(1) Parsing Table:


#Step 1: First check for left recursion in the grammar, if there is left recursion in the grammar remove that and go to step 2.

#Step 2: Calculate First() and Follow() for all non-terminals.

#First(): If there is a variable, and from that variable, if we try to drive all the strings then the beginning Terminal Symbol is called the First.
#Follow(): What is the Terminal Symbol which follows a variable in the process of derivation.
#Step 3: For each production A –> α. (A tends to alpha)


#Find First(α) and for each terminal in First(α), make entry A –> α in the table.
#If First(α) contains ε (epsilon) as terminal than, find the Follow(A) and for each terminal in Follow(A), make entry A –> α in the table.

#If the First(α) contains ε and Follow(A) contains $ as terminal, then make entry A
#–> α in the table for the $.
#To construct the parsing table, we have two functions:
#In the table, rows will contain the Non-Terminals and the column will contain the Terminal Symbols. All the Null Productions of the Grammars will go under the Follow elements and the remaining productions will lie under the elements of the First set.


#Code:
#
import re
import pandas as pd
def parse(user_input, start_symbol, parsingTable): flag = 0
user_input = user_input + "$" stack = []
stack.append("$") stack.append(start_symbol) input_len = len(user_input) index = 0
while len(stack) > 0:
top = stack[len(stack) - 1] print("Top =>", top)
current_input = user_input[index] print("Current_Input => ", current_input) if top == current_input:
stack.pop()
index = index + 1 else:
key = top, current_input print(key)
if key not in parsingTable: flag = 1
break
value = parsingTable[key] if value != '@':
value = value[::-1] value = list(value) stack.pop()
for element in value: stack.append(element)
else:
stack.pop() if flag == 0:
print("String accepted!") else:
print("String not accepted!") def ll1(follow, productions):
print("\nParsing Table\n") table = {}
for key in productions:
for value in productions[key]: if value != '@':
for element in first(value, productions): table[key, element] = value
else:
for element in follow[key]: table[key, element] = value
for key, val in table.items():
print(key, "=>", val) new_table = {}
for pair in table: new_table[pair[1]] = {}
for pair in table: new_table[pair[1]][pair[0]] = table[pair]
print("\n\nTable\n") print(pd.DataFrame(new_table).fillna('-')) print("\n")
return table
def follow(s, productions, ans):
if len(s) != 1: return {}
for key in productions:
for value in productions[key]: f = value.find(s)
if f != -1:
if f == (len(value) - 1): if key != s:
if key in ans:
temp = ans[key] else:
ans = follow(key, productions, ans) temp = ans[key]
ans[s] = ans[s].union(temp)
else:
first_of_next = first(value[f + 1:], productions) if '@' in first_of_next:
if key != s:
if key in ans:
temp = ans[key] else:
ans = follow(key, productions, ans) temp = ans[key]
ans[s] = ans[s].union(temp)
ans[s] = ans[s].union(first_of_next) - {'@'}
else:
ans[s] = ans[s].union(first_of_next)
return ans
def first(s, productions): c = s[0]
ans = set()
if c.isupper():
for st in productions[c]: if st == '@':
if len(s) != 1:
ans = ans.union(first(s[1:], productions)) else:
ans = ans.union('@')
else:
f = first(st, productions)
ans = ans.union(x for x in f)
else:
ans = ans.union(c) return ans
if 		name 	== " 	main 	": productions = dict()
grammar = open("grammar", "r") first_dict = dict()
follow_dict = dict() flag = 1
start = ""
for line in grammar:
l = re.split("( |->|\n|\||)*", line)
line = line.replace(" ", "").replace("\n", "") l = line.split("->")
lhs = l[0]
rhs = set(l[1:-1]) - {''} rhs = l[1].split("|")
if flag:
flag = 0 start = lhs
productions[lhs] = rhs print('\nFirst\n')
for lhs in productions:
first_dict[lhs] = first(lhs, productions) for f in first_dict:
print(str(f) + " : " + str(first_dict[f])) print("")
print('\nFollow\n')
for lhs in productions: follow_dict[lhs] = set()
follow_dict[start] = follow_dict[start].union('$') for lhs in productions:
follow_dict = follow(lhs, productions, follow_dict) for lhs in productions:
follow_dict = follow(lhs, productions, follow_dict) for f in follow_dict:
print(str(f) + " : " + str(follow_dict[f])) ll1Table = ll1(follow_dict, productions)
