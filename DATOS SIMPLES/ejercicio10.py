peso_payaso = 112
peso_muñecas = 75

num_payasos = float(input("Introduce el numero de payasos: "))
num_muñecas = int(input("Introduce el numero de muñecas: "))

peso_total = (num_payasos * peso_payaso) + (num_muñecas * peso_muñecas)

print (f"El peso total es: {peso_total} gramos.")
print (f"Equivale a {peso_total / 1000:.2f} en kilogramos")
