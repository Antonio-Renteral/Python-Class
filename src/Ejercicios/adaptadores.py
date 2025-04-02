inputfile = "data/Ejercicios/4_input_adapters.txt"
outputfile = "results/Ejercicios/4_input_no_adapters.txt"

#Abrir y leer el arhivo de entrada 4_input_adapters.txt
with open(inputfile,"r") as infile, open(outputfile,"w") as outfile:
    for linea in infile:

        #Cortar adaptadores son los primeros 1-14 caracteres de cada secuencia
        secuencia_limpia = linea.strip()[14:] #Eliminar caracteres de control a la izq y der y solo toma del caracter 14 en adelante

        #Mandar la salida a un archivo 4_input_no_adapters.txt
        outfile.write(f"{secuencia_limpia}\n")

        #Opcion alterna para imprimir el archivo
        #print(secuencia_limpia, file=outfile, end="\n")