# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros
# con dos decimales y muestre por pantalla el número de euros y el número de céntimos

precio = input("Introduce el precio (ej: 12.45): ")
partes = precio.split('.')
print(f"Euros: {partes[0]}")
print(f"Céntimos: {partes[1]}")

print("-" * 30)