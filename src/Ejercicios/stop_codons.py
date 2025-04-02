#Solicitamos al usuario que ingrese una serie secuencias de DNA separadas por comas
secuencias = input("Dame secuencias de DNA separadas por comas:\n").upper().split(",")

#Definimos una lista de codones de paro
stop_codons = ["TAA", "TAG", "TGA"]

#Usamos una comprension de listas para identificar las secuencias que contienen al menos un codón de parada.
#Para cada secuencia (seq) en "secuencias", verificamos si contiene algun codon de "stop_codons" usando any().
secuencias_con_stop_codon = [seq for seq in secuencias if any(codon in seq for codon in stop_codons)]

#Imprimimos un mensaje indicando que estas son las secuencias con codones de parada
print("Secuencias que contienen un stop codon:")
#Imprimimos la lista de secuencias que contienen al menos un codón de parada
print(secuencias_con_stop_codon)

#   Codigo de Hely:

#   secuencias_stop = [secuencia for secuencia in secuencias if "TAA" in secuencia or "TAG" in secuencia or "TGA" in secuencia]
#   print(secuencias_stop)