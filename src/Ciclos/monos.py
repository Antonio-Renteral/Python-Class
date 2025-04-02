apes = ["Pongo pygmaeus", "Pan troglodytes", "Gorilla gorilla"]

for ape in apes:
    print(f"{ape} is an ape. Its name start with {ape[0]}")
    print(f"Its name has {len(ape)}")

    #Escrito de otra forma puede ser:
    #name_length = len{ape}
    #first_letter = ape[0]
    #print(ape + " is an ape. Its name start with " + first_letter)
    #print("Its name has " + name_length)