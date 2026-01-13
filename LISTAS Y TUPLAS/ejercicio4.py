# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
# a mayor.

num = input("Dime los números ganadores (separados por espacio):"). split()
num.sort()
print("Ordenados: ", num)