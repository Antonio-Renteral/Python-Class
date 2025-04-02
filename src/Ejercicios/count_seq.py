inputfile = "results/Ejercicios/dna_sequences.fa"

with open(inputfile,"r") as infile:
    lineas = infile.readlines()

lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
print(len(lineas_filtradas))