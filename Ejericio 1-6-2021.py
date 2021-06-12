import sys
import os
import platform
from datetime import datetime
ip = input ("Ingrese la direccion IP: ")
IpDividida = ip.split('.')
print (IpDividida)

try:
	red = IpDividida[0]+'.'+IpDividida[1]+'.'+IpDividida[2]+'.'
	comienzo = int(input("Ingrese el numero de comienzo de la red: "))
	fin = int(input("Ingrese el numero en el que desea hacer el barrido: "))

except:
	print ("[!] Error")
	sys.exit(1)
	
print ("[*] Es escaneo se esta realizando desde ", red+str(comienzo), "hasta", red+str(fin))

for subred in range (comienzo, fin+1):
	direccion = red+str(subred)
	print (direccion)
	response = os.popen("ping"+" "+direccion)
	for line in response.readlines():
		if ("ttl" in line.lower()):
			print (direccion, "esta activo")
		if ("inaccesible" in line.lower()):
			print (direccion, "esta inactivo")
			break
