#Especificamos las rutas relativas de los archivos de entrada y de salida respectivamente
inputfile = "data/Ejercicios/dna_sequences.txt"
outputfile = "results/Ejercicios/dna_sequences.fa"

#Abrimos el archivo de entrada en modo lectura ("r") y el archivo de salida en modo escritura ("w")
with open(inputfile,"r") as infile, open(outputfile,"w") as outfile:

    #Iteramos sobre cada linea del archivo
    for linea in infile:

        #Eliminamos los caracteres de control al inicio y final de la linea con strip()
        #Dividimos la linea en dos partes usando "\t" como separador: ID y la secuencia
        id, seq = linea.strip().split("\t")

        #Escribimos las secuencias en el archivo de salida en formato FASTA
        outfile.write(f">{id}\n{seq.upper()}\n")