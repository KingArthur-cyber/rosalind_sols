import re
s = '16892 16007 16265 19470 18622 18845'
search = re.findall(r'[0-9]*',s)
lis = []

lis.append(search)
for i in search:
    if i == '':
        search.remove(i)
print(search)

one,two,three,four,five,six = 0,0,0,0,0,0
for i in range(0,len(search)):
    if i == 0:
        if int(search[i]) != 0:
            one = int(search[i]) * 2 * 1
            
        else:
            one = 0
    elif i == 1:
        if int(search[i]) != 0:
            two = int(search[i]) * 2 * 1
            
        else:
            two = 0
    elif i == 2:
        if int(search[i]) != 0:
            three = int(search[i]) * 2 * 1
            
        else:
            three = 0
    elif i == 3:
        if int(search[i]) != 0:
            four = float(search[i]) * (3/4) * 2
            
        else:
            four = 0
    elif i == 4:
        if int(search[i]) != 0:
            five = float(search[i]) * (1/2) * 2 
            
        else:
            five = 0
    else:
        six = 0
summation = one + two + three + four + five + six 
print(summation)    
        
