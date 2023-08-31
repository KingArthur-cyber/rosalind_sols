from Bio import Entrez

term = "Psammathodoxa"
start = "2002/12/13"
end = "2012/06/11"

Entrez.email = 'emsaundwalm@gmail.com'
handle = Entrez.esearch(db="nucleotide", term='"' + term + '"[Organism] AND ("' + start + '"[PDAT] : "' + end + '"[PDAT])"')
record = Entrez.read(handle)
print(record["Count"])
