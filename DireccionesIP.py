import os
from datetime import date
from datetime import datetime

# Defino el contador
contador = 0

# Cuento la cantidad de lineas en el archivo de direcciones IP
CantidadLineas = len(open('C:\Programas\DireccionesIP.txt').readlines())

# Defino la hora y fecha
Hoy = datetime.now() 
HoyHora = Hoy.strftime('Dia: %d/%m/%Y, Hora: %H:%M:%S')
# Defino la variable a escribir en el archivo HTML
Fecha_A_Mostrar = '<p style="text-align: center;"><strong>' + HoyHora + 'AM<br /></strong></p>'

# Antes de crear el arhivo verifico si existe, si existe lo borro
if os.path.exists('C:\Programas\DireccionesIP.html'):
    os.remove('C:\Programas\DireccionesIP.html')
else: 
    # Abro el archivo HTML
    ArchivoHTML = open ('C:\Programas\DireccionesIP.html', 'w')
    # Creo el titulo
    ArchivoHTML.write ('<h3 style="text-align: center;"><strong>&nbsp;***Verificacion de Host ITI ***</strong></h3> \n')
    # Escribo dia y hora de creacion del archivo
    #ArchivoHTML.write ('<p style="text-align: center;"><strong>2021-04-28 7:55:44 AM<br /></strong></p> \n')
    ArchivoHTML.write (Fecha_A_Mostrar)
    # Creo la tabla
    ArchivoHTML.write ('<table class="demoTable" style="height: 113px; width: 318px; margin-left: auto; margin-right: auto;" cellspacing="1" cellpadding="2"> \n')
    ArchivoHTML.write ('	<thead> \n')
    ArchivoHTML.write ('		<tr style="height: 55px;"> \n')
    ArchivoHTML.write ('		<tr style="height: 55px;"> \n')
    ArchivoHTML.write ('			<td style="width: 94.7667px; height: 55px;"><span style="color: #c82828;">Nombre Host</span></td> \n')
    ArchivoHTML.write ('			<td style="width: 94.7667px; height: 55px;"><span style="color: #c82828;">Estado</span></td> \n')
    ArchivoHTML.write ('		</tr>\n')
    ArchivoHTML.write ('	<thead> \n')
    ArchivoHTML.write ('	<tbody> \n')
    # Abro el archivo con las direcciones IP a usar
    ArchivoIP = open('C:\Programas\DireccionesIP.txt')
    for DireccionIP in ArchivoIP:
        Respuesta = os.system("ping 1" + DireccionIP)
        if Respuesta == 0:
            Estado = "Prendida"
            # Defino las variables a mostrar
            DireccionIP_A_Mostrar = ('		<td style="width: 94.7667px; height: 29px;">' + DireccionIP + '</td>')
            Estado_A_Mostrar = ('<td style="width: 94.7667px; height: 29px;">' + Estado + '</td>')
            ArchivoHTML.write ('		<tr style="height: 29px;">\n')
            ArchivoHTML.write (DireccionIP_A_Mostrar)
            ArchivoHTML.write (Estado_A_Mostrar)
            ArchivoHTML.write ('		</tr>\n')
        else:
            Estado = "Apagada"
            # Defino las variables a mostrar
            DireccionIP_A_Mostrar = ('		<td style="width: 94.7667px; height: 29px;">' + DireccionIP + '</td>')
            Estado_A_Mostrar = ('<td style="width: 94.7667px; height: 29px;">' + Estado + '</td>')
            ArchivoHTML.write ('		<tr style="height: 29px;">\n')
            ArchivoHTML.write (DireccionIP_A_Mostrar)
            ArchivoHTML.write (Estado_A_Mostrar)
            ArchivoHTML.write ('		</tr>\n')
    
    ArchivoHTML.write ('	<tbody> \n')
    ArchivoHTML.write ('<table> \n')
    ArchivoHTML.write ('<p style="text-align: center;">&nbsp;</p> \n')
    ArchivoHTML.write ('<p>&nbsp; &nbsp; &nbsp;&nbsp; .</p> \n')

    ArchivoHTML.close()


