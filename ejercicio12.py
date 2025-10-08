BarraDePan = 3.49
Descuento = 0.60

NumeroDeBarras = int(input("De barras que no son del dia se han vendido: "))

PrecioConDescuento = BarraDePan - Descuento
Total = NumeroDeBarras * PrecioConDescuento



print(f"El precio habitual es {BarraDePan:.2f} euros")
print(f"Con el descuento al no ser del dia se queda en: {PrecioConDescuento:.2f}")
print(f"El total a pagar por el {NumeroDeBarras} es {Total:.2f}.")