# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas.
# Ingredientes vegetarianos: Pimiento y Tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
# y según lo que responda, mostrarle un menú con los ingredientes disponibles para elegir.
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate
# (que siempre están en todas las pizzas).
#
# Al final se debe mostrar si la pizza es vegetariana o no y todos los ingredientes que lleva.

tipo = input("¿Pizza vegetariana? (si/no): ")

if tipo.lower() == "si":
    vegetariana = True
    ingrediente = input("Elige ingrediente (pimiento/tofu): ")
else:
    vegetariana = False
    ingrediente = input("Elige ingrediente (peperoni/jamon/salmon): ")

print("Ingredientes: mozzarella, tomate y", ingrediente)

if vegetariana:
    print("Pizza vegetariana")
else:
    print("Pizza NO vegetariana")
