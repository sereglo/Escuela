# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	sueldo = float()
	print("Ingrese horas trabajadas")
	horastrabajadas = float(input())
	print("Ingrese Valor de la hora")
	valorhoras = float(input())
	if horastrabajadas<=160:
		sueldo = horastrabajadast*valorhorash
	else:
		if horastrabajadas<=200:
			horasextras = horastrabajadas-160
			sueldo = (160*valorhoras)+(horasextras*(valorhoras*1.5))
		else:
			horasextras = horastrabajadas-200
			sueldo = (160*valorhoras)+(40*(valorhoras*1.5))+(horasextras*(valorhoras*2))
	if sueldo<=5000:
		sueldo = sueldo*0.95
	print("Su sueldo es: ",sueldo)

