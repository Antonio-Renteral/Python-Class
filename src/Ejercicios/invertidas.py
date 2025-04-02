secuencias = input("Dame secuencias separadas por comas:\n").split(",")

secuencia_invertida = [secuencia.strip()[::-1] for secuencia in secuencias]

print(secuencia_invertida)