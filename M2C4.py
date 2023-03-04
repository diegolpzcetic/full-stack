# Ejercicio 1

from decimal import Decimal

lista = ["perro", "gato"]
print(lista)

tupla = ("casa", 5, "coche")
print(tupla)

num_float = 42.5
print(num_float)

num_integer = 100
print(num_integer)

num_decimal = Decimal(3.14)
print(num_decimal)

diccionario = {"futbol": "Messi", "baloncesto": "Jordan"}
print(diccionario)

# Ejercicio 2
import math

rounded = math.ceil(num_float)
print(rounded)

# Ejercicio 3
num_float_sqrt = math.sqrt(num_float)
print(num_float_sqrt)

# Ejercicio 4
first_element = diccionario["futbol"]
print(first_element)

# Ejercicio 5
second_element = tupla[1]
print(second_element)

# Ejercicio 6
lista.append('oso')
print(lista)

# Ejercicio 7
lista[0] = "pájaro"
print(lista)

# Ejercicio 8
lista.sort()
print(lista)

# Ejercicio 9
tupla += ("avión", )
print(tupla)
