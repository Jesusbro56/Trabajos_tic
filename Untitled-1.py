nombre = input("ingrese el nombre del empleado;")
pago_hora = float(input("ingrese el pago por hora: $"))
horas_mes = float("ingrese las horas trabajadas al mes")
sueldo = pago_hora * horas_mes

if sueldo >= 100 and suelo <=300:
    bono = 500
elif sueldo >300 and sueldo <=1500:
    bono = 1700    
elif sueldo >300 and sueldo <=1500:
    bono = 1700     
elif sueldo >1500 and sueldo <=3000:
    bono = 3500 
elif sueldo >3000 and sueldo <=8000:
    bono = 8500
else:
    bono = 10000

sueldo_total = sueldo + bono

print("RESULTADOS DELEMPLEADO")
print("Nombre del empleado:", nombre)
print("Bono asignado: $",bono)