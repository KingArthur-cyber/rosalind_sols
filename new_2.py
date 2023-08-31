'''def caller(read):
    seed = [read[0]]
    
    for i in read:
        ret=locusfinder(seed[0],i)
        print(ret)
        seed+=ret
    
    print(seed)
'''
        
def foreachlocus(txt1,txt2,locuses):
    res = []
    for i in locuses:
        ret = traverse(txt1,txt2,i)
        res +=[ret]
    print(res)


def locusfinder(txt1,txt2):
    f1 = txt2[0]
    locuses = []
    for i in range(len(txt1)):
        if txt1[i] == f1:
            locuses+=[i]
    foreachlocus(txt1,txt2,locuses)

        
def stringmaker(txt1,txt2,locus1,Tru):
    if Tru==False:
        pass
    else:
        string=txt1[:locus1]+txt2
        return string

def traverse(txt1,txt2,locus1):
    k = True
    strn = ""
    if txt2 in txt1:
        k =False
    if k!=False:
        for i in range(len(txt2)-locus1):
            if txt1[i] == txt2[i+locus1]:
                pass
            else:
                k=False
        if k == True:
            strn = stringmaker(txt1,txt2,locus1,k)
            return strn
    return txt1

'''
file = open('genome.txt')
txt = file.read()
reads = txt.split("\n")
read = []

for i in reads:
    if ">" in i:
        pass
    else:
        read+=[i]
        
print(read)
'''
#this part takes one read and aligns other read and then aligned 
#read is aligned to next read 

locusfinder('ATTAGACCTGCCGGAA','GCCGGAATAC')