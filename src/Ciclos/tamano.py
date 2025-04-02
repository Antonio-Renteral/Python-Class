with open("genes.gff") as file:
    for linea in file:
        columnas = linea.strip().split("\t") #Strip es para quitar caracteres en blanco de ambos extremos de una cadena
        tamano = int(columnas[4])-int(columnas[3])+1 #Se le suma uno porque al restar perdemos uno
        print(tamano)