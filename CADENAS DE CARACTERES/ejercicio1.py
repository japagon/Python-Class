#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.

nombre = input("¿Cuál es tu nombre? ")
numero = int(input("¿Cuántas veces quieres que se repita? "))

for i in range(numero):
    print(nombre)

print("-" * 30)