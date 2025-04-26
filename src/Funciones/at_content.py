def at_content(dna, sig_figs):
    dna = dna.upper()
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count)/length
    return round(at_content, sig_figs)

result = at_content("atatatata", 1)
print(result)

result = at_content(significant_figures=5, dna="AGCTAGCTA")
print(result)

result = at_content(dna="ATCGATCGATCGACG", significant_figures=6)
print(result)