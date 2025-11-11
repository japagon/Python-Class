# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo, de altura el número introducido.

numero_entero = int(input("Introduce un numero entero: "))

for i in range(1, numero_entero + 1):

# Cuando usamos * sirve para repetir una cadena tantas veces como se indique.
    print("*" * i)