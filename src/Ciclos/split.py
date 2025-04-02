texto = "ATG CGT TAA GGC"
lista = texto.split() #Usa espacios en blanco para dividir la cadena
print(lista)

secuencia = "ATG,CGT,TAA,GGC"
lista = secuencia.split(",") #Usa comas para dividir la cadena
print(lista)

secuencia = "ATG-CGT-TAA-GGC"
lista = secuencia.split("-", 2) #Usa guiones para dividir la cadena, el dos es para ver cuantos vas a tomar para separar (max split)
print(lista)