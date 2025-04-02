inputfile = "data/Ejercicios/dna_sequences.txt"
outputfile = "results/Ejercicios/dna_sequences.fa"

with open(inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for linea in infile:
        id, seq = linea.strip().split("\t")
        outfile.write(f">{id}\n{seq.upper()}\n")