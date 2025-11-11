# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
# correcta.
contraseña = "contraseña"
entrada = input("¿Introduce la contraseña?")

while entrada != contraseña:
    print("Contraseña incorrecta, intentalo de nuevo")
    entrada = input("Introduce la contraseña: ")


print("Contraseña correcta ")