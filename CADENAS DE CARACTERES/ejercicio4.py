# Ejercicio 4
# Los teléfonos tienen formato prefijo-número-extension
# Mostrar el número sin prefijo ni extensión

telefono = input("Introduce un teléfono (+34-XXXXXXXXX-XX): ")
partes = telefono.split('-')
print(f"El número sin prefijo ni extensión es: {partes[1]}")

print("-" * 30)