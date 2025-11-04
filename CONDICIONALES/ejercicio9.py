# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular automáticamente el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años entra gratis.
# Si tiene entre 4 y 18 años paga 5€.
# Si tiene más de 18 años paga 10€.

edad = int(input("Cual es tu edad: "))

if edad < 4:
        entrada = "Gratis"
elif edad < 18:
        entrada = "Paga 5$"
elif edad > 18:
        entrada = "Paga 10$"
else :
    edad = None

if edad is None:
       print("Edad introducida no valida")
else :
       print("Debes de pagar: ", entrada)


