#Pedimos al usuario una serie de secuencias separadas por comas
secuencias = input("Dame secuencias separadas por comas:\n").upper().split(",")

#Usamos una comprension de listas para contar la cantidad de nucleotidos que hay en cada secuencia
#Para cada secuencia de la lista se genera una sublista
conteo = [[f"A: {secuencia.count('A')}", f"T: {secuencia.count('T')}", f"G: {secuencia.count('G')}", f"C: {secuencia.count('C')}"] for secuencia in secuencias]

#Imprimimos nuestro resultado para que el usuario pueda verlo
print(conteo)