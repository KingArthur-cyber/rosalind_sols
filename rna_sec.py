import math


def rna(seq):
    n1 = seq.count('A')
    n2 =  seq.count('G')
    result = math.factorial(n1) * math.factorial(n2)
    return result
print(rna('CCUUCACAUGCCGCUGUGUCAGCACGUUUGAGAGAAACAAGGUCUAAUGUGAUCCUGUACGAAGGCUAUUCA'))
