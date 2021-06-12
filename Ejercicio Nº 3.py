"""
Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales. 
Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica 
que es una vocal.
"""

oracion = input("Ingrese un texto: ")
contador = 0
for letra in oracion:
    if letra.lower() in "aeiou":
        contador += 1

print (contador)