# Ejercicio 1 (2ptos)
while True:
    funciones = input("¿Que desea hacer? (Consultar Saldo, Ingresar Dinero, Retirar Dinero, salir): ")
    if  funciones == "salir":
        break

    saldo = 1000

    if funciones == "Consultar Saldo":
        print(f"Tu saldo es: {saldo}")

    elif funciones == "Ingresar Dinero":
        ingreso = int(input("Ponga la cantidad que desea ingresar: "))
        ingreso_calculo = saldo + ingreso
        print(f"Usted a ingresado: {ingreso} lo que le da un total de {ingreso_calculo}")

    elif funciones == "Retirar Dinero":
        while True:
            retiro = float(input("Ingrese la cantidad que desea retirar: "))
            if retiro >= saldo:
                print(f"Usted no puede retirar tanto dinero, su saldo es {saldo}")
                break
            else:
                retiro_calculo = saldo - retiro
                print(f"Usted a retirado: {retiro} lo que le da un total de {retiro_calculo}")

    else: 
        print("No se encuentra esa funcion. ")
