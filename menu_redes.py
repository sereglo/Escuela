# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).
# -*- coding cp-1252 -*-
import os
import msvcrt
import time

print ("SISTEMA DE DIAGNOSTICO RÁPIDO DE FALLAS EN RED")
print ("**********************************************")
print ("************ MENU ************")
print ("HERRAMIENTA PING SELECCIONA (1)")
print ("HERRAMIENTA TRACERT SELECCIONA (2)")
print ("HERRAMIENTA HOSTNAME SELECCIONA (3)")
print ("HERRAMIENTA IPCONFIG SELECCIONA (4)")
print ("HERRAMIENTA DNS SELECCIONA (5)")
print ("HERRAMIENTA GATEWAY SELECCIONA (6)")
        
if __name__ == '__main__':

        a = input()
        if int(a)==1:
                  print ("SE EJECUTARA PING")
                  os.system("ping 192.168.3.1")
        else :
                if int(a)==2:
                        print ("SE EJECUTARA TRACEROUTE")
                        
                        os.system("tracert 200.48.225.130")
                        time.sleep(20)
                        
                else:
                        if int(a)==3:
                                print ("SE EJECUTARA HOSTNAME")
                                os.system("hostname")
                                
                        else:
                                if int(a)==4:
                                        print ("SE EJECUTARA IPCONFIG COMPLETO")
                                        os.system("ipconfig /all > ip.txt")
                                        x=input()
                                        
                                        
                                else:
                                        if int(a)==5:
                                                print ("SE EJECUTARA ANALISIS DE DNS")
                                                os.system("ping 200.48.225.130")
                                                
                                        else:
                                                if int(a)==6:
                                                        print("SE EJECUTARA ANALISIS DE GATEWAY")
                                                        os.system("ping 192.168.3.1")
                                                else:
                                                        print("opcion incorrecta")
msvcrt.getch()
