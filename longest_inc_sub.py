file = "longest_inc_sub.txt"
with open(file) as f:
    lines = f.readlines()
    
length = lines[0].rstrip('\n')
length = int(length) + 1
num_list = []
for i in lines[1].split():
    num_int = int(i)
    num_list.append(num_int)
#print(num_list)
lis = [8,2,1,6,7,4,3,9]
parent_list_inc = []
temp_lis_dec = []
run = True
count1 = 0
count2 = 2




while run:
    
print(parent_list_inc)

        
'''
    #2nd List Part
    inc1 = [0]
    for x in range(count2,len(lis),2): 
        if x < len(lis)-1:
            minu = min(lis[x],lis[x-1],lis[x+1])
                
            if minu == lis[x]:
                if inc1[-1] < lis[x]:
                    inc1.append(lis[x])
            elif minu == lis[x-1]:
                if inc1[-1] < lis[x-1]:
                    inc1.append(lis[x-1])
            else:
                if inc1[-1] < lis[x+1]:
                    inc1.append(lis[x+1])
        
    if inc1[-1] < lis[-1]:
        inc1.append(lis[-1])
    
        
    if ((len(inc) or len(inc1)) > len(temp_lis_inc)): 
        
        if len(inc) > len(inc1):
            temp_lis_inc = inc
        else:
            temp_lis_inc = inc1
    
    #dec_list    
                    
    dec = [length]
    for i in range(count1,len(lis),2): 
        if i < len(lis)-1:
            maxu = max(lis[i],lis[i-1],lis[i+1])
                
            if maxu == lis[i]:
                if dec[-1] > lis[i]:
                    dec.append(lis[i])
            elif maxu == lis[i-1]:
                if dec[-1] > lis[i-1]:
                    dec.append(lis[i-1])
            else:
                if dec[-1] > lis[i+1]:
                    dec.append(lis[i+1])
        
    if dec[-1] > lis[-1]:
        dec.append(lis[-1])
    
    #2nd List Part
    dec1 = [length]
    for x in range(count2,len(lis),2): 
        if x < len(lis)-1:
            maxu = max(lis[x],lis[x-1],lis[x+1])
                
            if maxu == lis[x]:
                if dec1[-1] > lis[x]:
                    dec1.append(lis[x])
            elif maxu == lis[x-1]:
                if dec1[-1] > lis[x-1]:
                    dec1.append(lis[x-1])
            else:
                if dec1[-1] > lis[x+1]:
                    dec1.append(lis[x+1])
    if dec1[-1] > lis[-1]:
        dec1.append(lis[-1])
    
    if ((len(dec) or len(dec1)) > len(temp_lis_dec)): 
        print(temp_lis_dec)
        if len(dec) > len(dec1):
            temp_lis_dec = dec
        else:
            temp_lis_dec = dec1    
'''
    
#print(*temp_lis_dec)


             
            