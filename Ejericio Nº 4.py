"""
Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres. 
Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, 
en caso contrario mostrar un mensaje de error
"""

clave = str(input("Ingrese una clave mayor de 10 caracteres y menor a 20 caracters: "))
#print(len(clave))
if len(clave) >= 10 and len(clave) <= 20:
    print ("Clave valida")
else:
    print ("Clave no valida, no contiene los caracteres requeridos, caracteres ingresados: ", len(clave))

