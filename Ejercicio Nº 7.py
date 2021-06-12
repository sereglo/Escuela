"""
Se cuenta con la siguiente información:
Las edades de 5 estudiantes del turno mañana.
Las edades de 6 estudiantes del turno tarde.
Las edades de 11 estudiantes del turno noche.
Las edades de cada estudiante deben ingresarse por teclado.
a) Obtener el promedio de las edades de cada turno (tres promedios)
b) Imprimir dichos promedios (promedio de cada turno)
c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.
"""

suma_manana = 0
suma_tarde = 0
suma_noche = 0
promedio_manana = 0 
promedio_tarde = 0 
promedio_noche = 0 
promedio_mayor = 0

for alumnos_manana in range(5):
    edad_manana = int(input("Ingrese la edad de los 5 alumons de la mañana: "))
    suma_manana = suma_manana + edad_manana

promedio_manana = suma_manana / 5

for alumnos_tarde in range(6):
    edad_tarde = int(input("Ingrese la edad de los 5 alumons de la tarde: "))
    suma_tarde = suma_tarde + edad_tarde

promedio_tarde = suma_tarde / 6

for alumnos_noche in range(11):
    edad_noche = int(input("Ingrese la edad de los 5 alumons de la noche: "))
    suma_noche = suma_noche + edad_noche

promedio_noche = suma_noche / 11

if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    promedio_mayor = "turno mañana"
else:
    if promedio_tarde > promedio_noche:
        promedio_mayor = "turno tarde"
    else:
        promedio_mayor = "turno noche"


print ("El promedio de edades del turno mañana es: ",promedio_manana)
print ("El promedio de edades del turno tarde es: ",promedio_tarde)
print ("El promedio de edades del turno noche es: ",promedio_noche)
print ("El ", promedio_mayor, "es el que tiene el mayor promedio")







    
