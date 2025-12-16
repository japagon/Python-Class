# Ejercicio 2 (2ptos)

while True:
    operador = input("Introduce la operacion que deseas realizar (suma/resta/producto/cociente/potencia) o (salir): ")
    if operador == "salir":
        break

    operando1 = float(input("Introduce el primer numero: "))
    operando2 = float(input("Introduce el segundo numero: "))

    if operador == "suma":
        resultado = operando1 + operando2
        print(f"Su resultado es: {resultado}")
    elif operador == "resta":
        resultado = operando1 - operando2
        print(f"Su resultado es: {resultado}")
    elif operador == "producto":
        resultado = operando1 * operando2
        print(f"Su resultado es: {resultado}")
    elif operador == "cociente":
        resultado = operando1 / operando2
        print(f"Su resultado es: {resultado}")
    elif operador == "potencia":
        resultado = operando1 ** operando2
        print(f"Su resultado es: {resultado}")
    else:
        print("Datos mal introducidos")

