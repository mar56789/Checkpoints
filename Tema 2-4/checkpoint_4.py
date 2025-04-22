# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

import math
from decimal import Decimal

print("Exercise 1")

number= 3 + 1/7
integer= int(number)
float = float(number)
decimal = Decimal(number)
complex1 = complex(number)

print("número inicial =>  ", number)
print("entero => ", integer)
print("float / decimal => ",float)
print("decimal / decimal preciso =>  ", decimal)
print("num. cientificos / complex =>  ", complex1 )

lista = ["mono", "tiburón", "tucán", "ballena", "león", "jirafa", "canguro", "loro", "delfín", "cotorra"]

tuple = ("mono", "tiburón", "tucán", "ballena", "león", "jirafa", "canguro", "loro", "delfín", "cotorra")

dictionary_1 = {
    "terrestres": ["mono", "león", "jirafa", "canguro"],
    "aves": ["tucán", "loro", "cotorra"],
    "acuáticos": ["tiburón", "ballena", "defín"]
}

dictionary_2 = {
    "terrestres": "rinoceronte",
    "aves": "alcón",
    "acuáticos": "atún",
}

print("lista [] =>  ", lista)
print("tuple ()=> ", tuple)
print("diccionario {} => ",dictionary_1)
print("diccionario {} => ",dictionary_2)

# Exercise 2: Round your float up.

print("Exercise 2")
print("Redondear float hacia arriba=>  ", math.ceil(float))

# Exercise 3: Get the square root of your float.

print("Exercise 3")
square = math.sqrt(float)
print('Exponents - square root =>  ', square)

# Exercise 4: Select the first element from your dictionary.


print("Exercise 4")

print("diccionario 1 - 1er elemento => ", list(dictionary_1.items())[0])
print("diccionario 1 - 1ra clasificación A => ", list(dictionary_1.keys())[0]) 
print("diccionario 1 - 1ra clasificación B => ", list(dictionary_1.items())[0][0])
print("diccionario 1 - 1er animal A => ",list(dictionary_1.values())[0][0])
print("diccionario 1 - 1er animal B => ",list(dictionary_1.items())[0][1][0])
element_1 = dictionary_1 ['terrestres'][0]
print("diccionario 1 - 1er animal C => ", element_1)



print("diccionario 2 - 1er elemento => ", list(dictionary_2.items())[0])
print("diccionario 2 - 1ra clasificación A => ", list(dictionary_2.keys())[0])
print("diccionario 2 - 1ra clasificación B => ", list(dictionary_2.items())[0][0])
print("diccionario 2 - 1er animal A => ",list(dictionary_2.values())[0])
print("diccionario 2 - 1er animal B => ",list(dictionary_2.items())[0][1])
element_2 = dictionary_2 ['terrestres']
print("diccionario 2 - 1er animal C => ", element_2)


# Exercise 5: Select the second element from your tuple.

print("Exercise 5")

print("diccionario 1 - 1er elemento => ", list(dictionary_1.items())[0])
print("diccionario 1 - 2do elemento dentro del 1ro (animales A) => ", list(dictionary_1.values())[0])
print("diccionario 1 - 2do elemento dentro del 1ro (animales B) => ", list(dictionary_1.items())[0][1])

print("diccionario 2 - 1er elemento => ", list(dictionary_2.items())[0])
print("diccionario 2 - 2do elemento dentro del 1ro (animales A) => ", list(dictionary_2.values())[0])
print("diccionario 2 - 2do elemento dentro del 1ro (animales B) => ", list(dictionary_2.items())[0][1])



# Exercise 6: Add an element to the end of your list.

print("Exercise 6")

lista.extend(['ardilla'])
print("lista aumentada => ", lista)
lista.extend(['buitre'])
print("lista aumentada => ", lista)
lista.extend(['morena'])
print("lista aumentada => ", lista)

# Exercise 7: Replace the first element in your list.

print("Exercise 7")

lista[0] = "luciernaga"
print("cambiar 1er elemento => ", lista)

# Exercise 8: Sort your list alphabetically.

print("Exercise 8")

lista.sort()
print("Lista ordenada alfabeticamente => ", lista)

# Exercise 9: Use reassignment to add an element to your tuple.

print("Exercise 9")

print("tuple => ", tuple)
tuple += ('cabra',)
print("tuple => ", tuple)
tuple = tuple + ('oveja',)
print("tuple => ", tuple)
