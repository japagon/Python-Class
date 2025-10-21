peso = float(input("Peso (kg): ")) # Pedimos el peso, y con float convertimos el peso a numero decimal
altura = float(input("Altura (m): ")) # Pedimos la altura y con float convertimos a numero decimal
imc = peso / (altura ** 2) # Decimos que el IMC es la altura elevado a 2 entre el peso
print(f"IMC: {imc}") # Mostramos el IMC: 