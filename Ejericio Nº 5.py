"""
Dada la Lista ["Ana", 7, 9,'Pedro',8,7,'Juan',6,5,'Jose',8,9,'Luis',6,7], imostrar nombre y promedio
"""

Lista=["Ana", 7, 9,"Pedro",8,7,"Juan",6,5,"Jose",8,9,"Luis",6,7]

Promedio_Ana=float((Lista[1]+Lista[2])/2)
Promedio_Pedro=float((Lista[4]+Lista[5])/2)
Promedio_Juan=float((Lista[7]+Lista[8])/2)
Promedio_Jose=float((Lista[10]+Lista[11])/2)
Promedio_Luis=float((Lista[13]+Lista[14])/2)

print("El promedio de", Lista[0], "es" , Promedio_Ana)
print("El promedio de", Lista[3], "es" , Promedio_Pedro)
print("El promedio de", Lista[6], "es" , Promedio_Juan)
print("El promedio de", Lista[9], "es" , Promedio_Jose)
print("El promedio de", Lista[12], "es" , Promedio_Luis)