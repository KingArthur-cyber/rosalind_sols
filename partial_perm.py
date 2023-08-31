import math
def get_permutation(string, i=0):
   
    if i == len(string):   	 
        print(" ".join(string))

    for j in range(i, len(string)):
        
        words = [c for c in string]
   
        # swap
        words[i] , words[j] = words[j] , words[i]
   	 
        get_permutation(words, i + 1)
s = '123'
n = 80
k = 9
total = math.factorial(n)
partial = math.factorial(n-k)
final  =  (total/partial) 
print(final%1000000)
#x = get_permutation(s)
#print(x)