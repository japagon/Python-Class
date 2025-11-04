# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más,
# pero no valores intermedios entre esas cifras.
#
# Nivel        Puntuación
# Inaceptable  0.0
# Aceptable    0.4
# Meritorio    0.6 o más
#
# La cantidad de dinero que se consigue es 2400€ multiplicado por la puntuación.
#
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento
# y la cantidad de dinero que recibirá.

puntuacion = float(input("Introduce tu puntuacion: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
elif puntuacion < 0.4:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel is None:
    print("Puntuacion no valida")
else:
    dinero = 2400 * puntuacion

    print("Tu nivel es: ", nivel)
    print("Te corresponde: ", dinero, " $.")