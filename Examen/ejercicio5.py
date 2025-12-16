# Ejercicio 5 (2ptos)

cantidad = int(input("Introduce una cantidad: "))

moneda10 = cantidad // 10
cantidad = cantidad - moneda10 * 10

moneda5 = cantidad // 5
cantidad = cantidad - moneda5 * 5

moneda2 = cantidad // 2
cantidad = cantidad - moneda2 * 2

moneda1 = cantidad

print(f"Puede usar {moneda10} billetes de 10")
print(f"Puede usar {moneda5} billetes de 5")
print(f"Puede usar {moneda2} monedas de 2")
print(f"Puede usar {moneda1} monedas de 1")