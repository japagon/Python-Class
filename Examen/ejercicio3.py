# Ejercicio 3 (2ptos)

renta = float(input("Introduce tu renta: "))
irpf = 0

if renta > 35200:
    irpf += (renta - 32500) * 0.37
    renta = 32500

if renta > 20200:
    irpf += (renta - 20200) * 0.30
    renta = 20200

if renta > 12450:
    irpf += (renta - 12450) * 0.24
    renta = 12450
 

irpf = irpf + renta * 0.19

print(f"El IRPF que debde pagar es: {irpf}")
    


