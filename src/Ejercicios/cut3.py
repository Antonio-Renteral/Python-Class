secuencias = input("Dame secuencias separadas por comas:\n").split(",")

codones_inicio = [secuencia[:3] for secuencia in secuencias]

print(codones_inicio)