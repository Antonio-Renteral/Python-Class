#Le pedimos una serie de secuencias al usuario que esten separadas por comas
secuencias = input("Dame secuencias separadas por comas:\n").split(",")

#utilizamos una comprension de listas para hacer la inversion
#[::-1] invierte la secuencia, devolviendo los caracteres en orden inverso.
secuencia_invertida = [secuencia.strip()[::-1] for secuencia in secuencias]

#Imprimimos la secuencia que el usuario nos dio pero de forma invertida
print(secuencia_invertida)