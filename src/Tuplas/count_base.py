secuencia = tuple("ATGCTTCGA")

# Forma 1 de contar:
print(secuencia.count("A"))
print(secuencia.count("T"))
print(secuencia.count("G"))
print(secuencia.count("C"))

# Forma 2 de contar (comprension de listas):
bases = list("ATGC")
freq = [(base, secuencia.count(base)) for base in bases]
print(freq)

# Forma 3 de contar (ciclos):
for base in "ACGT":
    print(f"{secuencia.count(base)} bases {base}")