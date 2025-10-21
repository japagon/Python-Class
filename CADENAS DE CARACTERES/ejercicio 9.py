# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fecha.split('/')
print(f"Día: {partes[0]}")
print(f"Mes: {partes[1]}")
print(f"Año: {partes[2]}")

print("-" * 30)