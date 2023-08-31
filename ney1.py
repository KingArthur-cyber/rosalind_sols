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