import pandas as pd

'''
Solo se puede usar un tipo de dato por fila o por columna, con que haya uno solo de un tipo,
todos se transforman en ese tipo de dato.
'''

# Lista indexada:
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

# Data frame:
data = {
    "Gene": ["thrL", "thrA", "thrB"],
    "Longitud": [117, 2340, 1461]
}
df = pd.DataFrame(data)
print(df)

# Si quisieramos que gene y longitud sean los indices:
data = {
    "Gene": ["thrL", "thrA", "thrB"],
    "Longitud": [117, 2340, 1461]
}
df = pd.DataFrame.from_dict(data, orient= "index")
print(df)

# Si quiseramos pedirle varias columnas hay que pasarlas como lista:
data = {
    "Gene": ["thrL", "thrA", "thrB"],
    "Longitud": [117, 2340, 1461]
}
df = pd.DataFrame(data)
print(df[["Gene"]])


#Si queremos uno en especifico podemos usar coordenadas:
data = {
    "Gene": ["thrL", "thrA", "thrB"],
    "Longitud": [117, 2340, 1461]
}
df = pd.DataFrame(data)
# Con indices y labels
print(df.loc[0, "Gene"])

data = {
    "Gene": ["thrL", "thrA", "thrB"],
    "Longitud": [117, 2340, 1461]
}
df = pd.DataFrame(data)
# Solo con indices
print(df.iloc[0, 0]) 

# Dataframe para hacer operaciones:
data = {
    "Nombre": ["Ana", "Luis", "Sofia"],
    "Edad": [28, 34, 22],
    "Ciudad": ["CDMX", "Guadalajara", "Monterrey"]
}
df = pd.DataFrame.from_dict(data, orient= "columns")
print(df)

# Otro dataframe para hacer operaciones:
genes = {
    'GeneID': ['b0001', 'b0002', 'b0003'],
    'Nombre': ['thrL', 'thrA', 'thrB'],
    'Función': ['regulador', 'enzima', 'enzima'],
    'Longitud': [117, 2340, 1461]
}
df_genes = pd.DataFrame(genes)
print(df_genes[(df_genes["Función"] == "enzima") & (df_genes["Longitud"] > 1000)]["GeneID"])

# Abrimos el archivo genes.gff:
df_csv = pd.read_csv("./../../data/Pandas/genes.gff", sep= '\t', comment= '#', header= None, names=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
print(df_csv)