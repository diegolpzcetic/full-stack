
# Ejercicio 1
var_string = "hola buenos días a todos"
var_number = 5
var_list = ["coche", "moto", "avión", 112]
var_boolean = True

print(var_string)
print(var_number)
print(var_list)
print(var_boolean)

#Ejercicio 2
var_three = var_string[0:3]
print(var_three)

#Ejercicio 3
print(var_list[0])

#Ejercicio 4
new_number = var_number +10
print(new_number)

#Ejercicio 5
print(var_list[-1])

#Ejercicio 6
names = 'harry,alex,susie,jared,gail,conner'
print(names.split(','))

#Ejercicio 7
words = var_string.split()
first_word = words[0].upper()
new_string = first_word + ' ' + ' '.join(words[1:])
print(new_string)


