# Programa para calcular el saldo de una cuenta de ahorros con interés compuesto

deposito = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04

saldo_1 = round(deposito * (1 + interes), 2)
saldo_2 = round(saldo_1 * (1 + interes), 2)
saldo_3 = round(saldo_2 * (1 + interes), 2)

print(f"Saldo tras el primer año: {saldo_1}")
print(f"Saldo tras el segundo año: {saldo_2}")
print(f"Saldo tras el tercer año: {saldo_3}")
