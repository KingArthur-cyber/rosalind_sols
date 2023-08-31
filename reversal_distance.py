s1_1 = "1 2 3 4 5 6 7 8 9 10"
s1_2 = "3 1 5 2 7 4 9 6 10 8"

s2_1 = "3 10 8 2 5 4 7 1 6 9"
s2_2 = "5 2 3 1 7 4 10 8 6 9"

s3_1 = "3 9 10 4 1 8 6 7 5 2"
s3_2 = "3 9 10 4 1 8 6 7 5 2"

s4_1 = "1 2 3 4 5 6 7 8 9 10"
s4_2 = "1 2 3 4 5 6 7 8 9 10"

s5_1 = "8 6 7 9 4 1 3 10 2 5"
s5_2 = "8 2 7 6 9 1 5 3 10 4"

s1 = s1_1.split(" ")
s2 = s1_2.split(" ")
def distance(s1,s2):
    score = 0
    distance_cost = []
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i] == s2[i]:
                score += 1
            elif ((s1[i] == s2[j]) and (i != j)):
                distance_cost.append([i,j])
                break
            
            else:
                score -= 1
    for i in range(0,len(distance_cost)):
        
                
            
distance_cost  = []
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s1[i] == s2[i]:
            pass
        elif ((s1[i] == s2[j]) and (i != j)):
            distance_cost.append([i,j])
            break
print(distance_cost)
        
        








def reversal_distance(s1,s2):
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    distance_cost  = []
    while s1 != s2:
        for i in range(0,len(s1)):
            for j in range(0,len(s2)):
                if s1[i] == s2[i]:
                    pass
                elif (s1[i] == s2[j]) and (i != j):
                    distance_cost.append([i,j])
                    break
           
                
                
            
