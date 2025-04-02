secuencias = input("Dame secuencias separadas por comas:\n").split(",")

secuencias_arn = [secuencia.replace("T","U") for secuencia in secuencias]

print(secuencias_arn)