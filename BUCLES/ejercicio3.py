# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla todos los números impares desde 1 hasta ese número separados por
# comas.

# Pedimos el numero entero positivo
numero = int(input("Dime un número positivo: "))

# Con esto generamos un bucle es decir "voy a repetir esto varias veces"
# empiza a contar desde uno y termina donde se ha establecido el numero
# usamos numero + 1 debido a que acaba uno antes.
for i in range(1, numero + 1):
    
# Como queremos saber los numeros impares, cuando el resultado sea 0
# significa que es par

# Usamos != que significa si es "distinto de..." 0
    if i % 2 != 0:

# Mostramos el numero en pantalla, pero en lugar de saltar a la siguiente linea
# le decimos que ponga una coma.
        print (i, end=", ")
