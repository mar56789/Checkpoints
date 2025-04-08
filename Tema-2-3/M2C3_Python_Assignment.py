# exercise 1
# Create a string, number, list, and boolean, each stored in their own variable.

string = "El perro de San Roque no tiene rabo, porque Ramón Ramírez se lo ha cortado"
number = 2645 
list = ["perro","gato","cerdo","vaca","gallina"] 
boolean= True

# exercise 2
# Use an index to grab the first 3 letters in your string, store that in a variable. 

first_3_letters = string [0:3]
print(first_3_letters)

#exercise 3
# Use an index to grab the first element from your list.

first = string [0]
print(first)

print(string[0])

# exercise 4
# Create a new number variable that adds 10 to your original number.
Number_two = number + 10

# exercise 5
# Use an index to get the last element in your list.

last = string [-1]
print(last)

print(string[-1])

#exercise 6
# Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)

# Exercise 7 
# Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

string = "El perro de San Roque no tiene rabo, porque Ramón Ramírez se lo ha cortado"

frist_word = string [0:2]
frist_word_up = frist_word.upper()
# also     frist_word_up = string [0:2].upper() 
print(frist_word_up)

string_two = string.replace(frist_word, frist_word_up)
print(string_two)

# Exercise 8 
# Use string interpolation to print out a sentence that contains your number variable.

year = 2025 
year_sentence = f"El año actual es {year}" 
print(year_sentence)

# Exercise 9:
# Print “hello world”.

print('hello world')

# Exercise 10:
# Crea una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".

chiste = """
- Hola, disculpe, ¿llegó Julio?
- No ...si apenas estamos en Abril!!!
"""

buscar_hola = chiste.find('Hola')
print(buscar_hola)

decir_adios= chiste.replace('Hola', 'Adiós')
print(decir_adios)


