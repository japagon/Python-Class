# Ejercicio 6

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
# el nombre. 

# El grupo A está formado por las mujeres con un nombre anterior a la M y
# los hombres con un nombre posterior a la N 

# El grupo B por el resto. 

# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
# que le corresponde.

nombre = input("Cual es tu nombre: ").upper()
sexo = input("Tu género: ").upper()


if(sexo == "M" and nombre < "M") or (sexo == "F" and nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print ("Te toca el grupo ", grupo)
