# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
# de la arroba @) pero con dominio ceu.es.

correo = input ("introduce el correo: ")

correoMod = correo.split("@")[0] + "@ceu.es"

print (f"Tu correo modificado es: {correoMod}")