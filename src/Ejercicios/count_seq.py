inputfile = "results/Ejercicios/dna_sequences.fa"

with open(inputfile,"r") as infile: #Con esto abrimos el archivo con el que vamos a trabajar
    lineas = infile.readlines()

#Usamos comprension de listas para filtrar unicamente las lineas que comienzan con ">"
lineas_filtradas = [linea for linea in lineas if linea.startswith(">")]
#Imprimimos la cantidad de lineas filtradas
print(len(lineas_filtradas))