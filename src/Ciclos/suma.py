#Map es una funcion que aplica una funcion a cada uno de los elemento de un iterable

numeros_str = input("Dame 3 numeros separados por espacio ").split()
lista_numeros = list(map(int,numeros_str))

suma = sum(lista_numeros)
print(suma)