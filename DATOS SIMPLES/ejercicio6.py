# Leer un entero positivo del usuario
n = int(input("Introduce un número entero positivo: "))

# Calcular la suma de 1 hasta n usando la fórmula matemática
suma = n * (n + 1) // 2 # La // es el consciente

# Mostrar el resultado
print(f"La suma de todos los enteros desde 1 hasta {n} es: {suma}")