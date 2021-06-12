"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.
"""

numeros_negativos = 0
numeros_positivos = 0
multiplo_de_15 = 0
suma_de_pares = 0

for numero_cargado in range(10):
    numeros_cargados = int(input("Ingrese 10 numeros positivos o nevativos: "))
    if numeros_cargados < 0:
        numeros_negativos += 1
    else:  
        if numeros_cargados > 0:
            numeros_positivos += 1
    if numeros_cargados % 15 == 0:
        multiplo_de_15 += 1
    if numeros_cargados % 2 == 0:
        suma_de_pares = suma_de_pares + numeros_cargados

print("La cantidad de numeros negativos es: ", numeros_negativos)
print("La cantidad de numeros positivos es: ", numeros_positivos)
print("La cantidad de numeros multiplos de 15 es: ", multiplo_de_15)
print("La suma de los numeros pares es: ", suma_de_pares)

