cantidad = float(input("Ingresa la cantidad a invertir: "))
interes = float(input("Ingresa el intéres anual: "))
años = int(input("Ingresa el capital obtenido: "))

CapitalFinal = cantidad * (1 + interes/100) ** años

print (f"El capital obtenido tras {años} años sera de {CapitalFinal:.2f} euros.")

#.2f sirve para que en ese numero salga con dos decimales.
