# Ejercicio 2
# Escribir un programa que almacene la contraseña en una variable, pregunte al usuario por la contraseña
# e imprima por pantalla si la contraseña introducida coincide con la guardada sin tener en cuenta mayúsculas y minúsculas.

contraseña_guardada = "secreta123"
contraseña_usuario = input("Introduce la contraseña: ")

if contraseña_usuario == contraseña_guardada:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

