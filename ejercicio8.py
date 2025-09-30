# Ejercicio 8: División con cociente y resto

# Pedir al usuario dos números enteros
n = int(input("Introduce el primer número entero (dividendo): "))
m = int(input("Introduce el segundo número entero (divisor): "))

# Calcular cociente y resto de la división entera
cociente = n // m
resto = n % m

# Mostrar el resultado formateado
print(f"{n} entre {m} da un cociente {cociente} y un resto {resto}")