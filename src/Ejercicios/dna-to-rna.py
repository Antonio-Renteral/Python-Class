#Solicitamos al usuario que nos de una serie de secuencias separadas por comas
secuencias = input("Dame secuencias separadas por comas:\n").split(",")

#utilizamos una comprension de listas
#Para cada secuencia en la lista, replace("T", "U") reemplaza la base nitrogenada Timina (T) por Uracilo (U)
secuencias_arn = [secuencia.replace("T","U") for secuencia in secuencias]

#Imprime la nueva secuencia que ahora sera de RNA
print(secuencias_arn)