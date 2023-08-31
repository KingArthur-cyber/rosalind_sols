from math import log10
def file_reader(file):
    with open(file) as f:
        lines = f.readlines()
        dna = lines[0].rstrip('\n')
        gc = lines[1].split(" ")
    return(dna,gc)
            
def calculate_prob(string,gc):
    sym_probs = {"G": log10(gc / 2.0), "C": log10(gc / 2.0), "A": log10((1.0 - gc) / 2.0), "T": log10((1.0 - gc) / 2.0)}
    log_probability = 0
    for sym in string:
        log_probability += sym_probs[sym]
    return log_probability
   

file = 'introduction_to_random_strings.txt'
final = []
for i in file_reader(file)[1]:
    i = float(i)
    
    final.append(round(calculate_prob(file_reader(file)[0],i),3))
print(' '.join(map(str, final)))