# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su
# división. Si el divisor es cero el programa debe mostrar un error.

num1 = int(input("Introduce el dividendo: "))
num2 = int(input("Introduce el divisor: "))

if num2 == 0:
    print("Error: El numero es 0 ")
else:
    resultado = num1 / num2
    print(f"Correcto el numero es {resultado}")

