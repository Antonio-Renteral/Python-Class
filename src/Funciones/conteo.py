def count_bases(dna, sig_figs):
    dna = dna.upper()
    conteo = {
        'A': dna.count('A'),
        'T': dna.count('T'),
        'G': dna.count('G'),
        'C': dna.count('C')
    }
    return conteo

dna = "ATGATGGTACAT"
resultado = count_bases(dna)