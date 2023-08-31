filename = "intro_to_bio_army.txt"
with open(filename) as f:
    lines = f.readlines()
    sequence = lines[0].strip("\n")
answer = [] 
a_count = 0 
c_count = 0
g_count = 0
t_count = 0
for base in sequence:
    if base == 'A':
        a_count += 1
    elif base == 'C':
        c_count += 1
    elif base == 'G':
        g_count += 1
    else:
        t_count += 1
answer.append(a_count)
answer.append(c_count)
answer.append(g_count)
answer.append(t_count)
print(*answer)

        
    
    