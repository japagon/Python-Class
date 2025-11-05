# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce un numero entero positivo: "))

# El primer -1 sirve para que se muestre el numero 0
# El segundo es para que reste uno cada vuelta
for numero in range(numero, -1, -1):
    print (numero, end=", ")