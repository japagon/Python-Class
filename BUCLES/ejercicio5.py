# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
# año que dura la inversión.

cantidad = float(input("¿Que cantidad desea invertir?: "))
interes = float(input("Introduce el interes anual (en %): "))
años = int(input("Introduce el número de años: "))


# Aqui creamos una secuencia de numeros desde 1 hasta el numero de años que se introduzca
for i in range(1, años + 1):

# Esta linea se encarga de actualizar el capital por cada año
# *= se encarga de multiplicar y guardar el resultado en la misma variable
    cantidad *= (1 + interes / 100)

print(f"Año {i}: capital = {cantidad:.2f}")

