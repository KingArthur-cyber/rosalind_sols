import numpy as np
file_name = "error_correction.txt"
with open(file_name) as f:
    new_dict = {}
    
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('>'):
            
            key = line.lstrip('>')
            new_dict[key] = []
        else:
            
            new_dict[key].append(line)

for key,value in new_dict.items():
    value = ''.join(value)
    new_dict[key] = value
value = []
for values in new_dict.values():
    value.append(values)
print(value)

def reverse_complement(string):
    rev_comp = ''
    if string == '':
        print("Please pass a string")
    else:
        string = string[::-1]
        for i in string:
            if i == 'A':
                rev_comp += 'T'
            elif i == 'T':
                rev_comp += 'A'
            elif i == 'C':
                rev_comp += 'G'
            else:
                rev_comp += 'C'
    return rev_comp
def hamming(string1,string2):
    score = 0
    for i in range(0,len(string1)):
        if string1[i] == string2[i]:
            pass
        else:
            score += 1
    return score
rev_comp_list = []
for i in range(0,len(value)):
    rev_comp_list.append(reverse_complement(value[i]))
incorrect_list = []
correct_list = []
for i in range(0,len(value)):
    for j in range(0,len(value)):
        if value[i] == rev_comp_list[j]:
            correct_list.append(value[i])
        if i == j:
            pass
        elif value[i] == value[j]:
            if value[i] not in correct_list:
                correct_list.append(value[i])
print("Correct List: ",correct_list,"\n")
print("Reverse Complement List: ",rev_comp_list,"\n")
for i in range(0,len(value)):
    for j in range(0,len(correct_list)):
        if value[i] == correct_list[j]:
            pass
        else:
            if value[i] not in correct_list:
                incorrect_list.append(value[i])
       
incorrect_list = list(set(incorrect_list))
print("Incorrect List: ",incorrect_list)
for i in range(0,len(correct_list)):
    correct_list.append(reverse_complement(correct_list[i]))
print(correct_list)
final_list = []
for i in range(0,len(incorrect_list)):
    for j in range(0,len(correct_list)):
        if hamming(correct_list[j],incorrect_list[i]) == 1:
            res = incorrect_list[i] + '->' + correct_list[j]
            if res not in final_list:
                final_list.append(res)
for i in final_list:
    print(i)

            