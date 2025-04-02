secuencias = input("Dame secuencias de DNA separadas por comas:\n").upper().split(",")

stop_codons = ["TAA", "TAG", "TGA"]

secuencias_con_stop_codon = [seq for seq in secuencias if any(codon in seq for codon in stop_codons)]

print("Secuencias que contienen un stop codon:")
print(secuencias_con_stop_codon)

#   Codigo de Hely:

#   secuencias_stop = [secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]
#   print(secuencias_stop)