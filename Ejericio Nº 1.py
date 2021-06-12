"""Diseñar un algoritmo que calcule y muestre el salario mensual de un empleado a partir de sus 
horas trabajadas y del valor hora establecido. La cantidad de horas trabajadas que superen 
las 160 se pagan aun valor de un 50% adicional. En cambio, las que superen las 200 se abonan 
al doble de su valor hora original. Al salario mensual calculado se le debe descontar un 5% 
en concepto de aportes y contribuciones siempre que su sueldo bruto no supere los $5000"""

HorasTrabajadasMayor160=0
HorasTrabajadasMayor200=0
HorasAdicionales=0
HorasExtras=0
HorasNormales=0
SueldoBruto=0
SueldoNeto=0
Descuento=0
HorasTrabajadas=float(input("Ingrese las horas trabajadas: "))
PagoHoras=float(input("Ingrese el valor de las horas: "))

if HorasTrabajadas >= 160 and HorasTrabajadas < 200:    
    HorasTrabajadasMayor160 = (HorasTrabajadas -160) 
    HorasAdicionales = HorasTrabajadas / 2
    HorasExtras = HorasTrabajadasMayor160 * HorasAdicionales
    HorasNormales = 160 * HorasTrabajadas
    SueldoBruto = HorasNormales + HorasExtras
    print(SueldoBruto)
if HorasTrabajadas > 200:
    HorasTrabajadasMayor200 = (HorasTrabajadas -160) 
    HorasAdicionales = HorasTrabajadas * 2
    HorasExtras = HorasTrabajadasMayor200 * HorasAdicionales
    HorasNormales = 160 * HorasTrabajadas
    SueldoBruto = HorasNormales + HorasExtras    
    print(SueldoBruto)
if HorasTrabajadas < 160:
    SueldoBruto = HorasTrabajadas * PagoHoras

if SueldoBruto > 5000:
    Descuento = (5 * SueldoBruto) / 100
    SueldoNeto = SueldoBruto - Descuento
else:
    SueldoNeto = SueldoBruto - Descuento

print(SueldoNeto)


