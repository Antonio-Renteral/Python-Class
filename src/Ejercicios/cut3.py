#Solicitamos al usuario que ingrese una serie de secuencias separadas por comas
#La función input captura la entrada del usuario en forma de texto
#split(",") divide la cadena ingresada en una lista de secuencias, separadas por la coma
secuencias = input("Dame secuencias separadas por comas:\n").split(",")

#Uso de comprension de listas para obbtener los primeros tres caracteres
codones_inicio = [secuencia[:3] for secuencia in secuencias]

#Imprimimos el resultado obtenido
print(codones_inicio)