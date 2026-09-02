import os 
os.system ("cls")

#CarreraRecargo
Recargo_Ingenieria	= 50000
Recargo_Medicina = 100000
Recargo_Derecho = 3000
Recargo_Pedagogia = 0
Recargo_Enfermeria	= 40000

nombre = input("ingrese nombre del estudiante: ")
Edad = int(input("ingrese edad: "))
nem = int(input("ingrese NEM del estudiante: "))
carrera = int(input("ingrese carrera que desea estudiar 1)ingenieria  2)Medicina 3)Derecho 4)Pedagogia 5)Enfermaria: "))
beca = input("Si tiene alguna beca (si / no)")
fam_funcionario = input("¿Es familiar de un funcionario de la universidad? (si / no)")
#________________________________________

Matricula_base = 180000

#Si el estudiante ingresa una carrera que no está en las opciones anteriores, se debe informar que la carrera no está disponible.
#________________________________________

if carrera == "1":
    eleccion_carrera = "ingenieria"
    valor_final = Matricula_base + Recargo_Ingenieria
elif carrera == "2":
    eleccion_carrera = "Medicica"
    valor_final = Matricula_base + Recargo_Medicina
elif carrera == "3":
    eleccion_carrera = "Derecho"
    valor_final = Matricula_base + Recargo_Derecho
elif carrera == "4":
    eleccion_carrera = "Pedagogia"
    valor_final = Matricula_base + Recargo_Pedagogia
elif carrera == "5":
    eleccion_carrera = "Enfermeria"
    valor_final = Matricula_base + Recargo_Enfermeria
else:
    print("la carrera no esta disponible")
    
#Descuentos según NEM
if nem >= 6.5 and nem <=7.0: 
    descuento = 0.30
elif nem >= 6.0 and nem <= 6.49:
    descuento = 0.20
elif nem >= 5.5 and nem <= 5.99:
    dscuento = 0.10
else:
    ("No tiene descuento")
#El estudiante puede obtener un descuento dependiendo de su NEM:
#NEM	Descuento
#6.5 a 7.0	30%
#6.0 a 6.49	20%
#5.5 a 5.99	10%
#Menor a 5.5	0%
#Por ejemplo:
#NEM: 6.7
#Descuento: 30%
#________________________________________
#Descuento por beca
#Si el estudiante tiene beca:
#si → 15% de descuento adicional
#no → 0%
#Pero hay una condición importante:
#El descuento máximo acumulado no puede superar el 40%.
#Por lo tanto, si un estudiante obtiene:
#30% por NEM
#15% por beca
#No recibe 45%, sino 40%.
#Esto permite que practiquen bastante con operadores lógicos.
#________________________________________
#Descuento familiar
#Si el estudiante es familiar de un funcionario:
#10% adicional
#Pero nuevamente se mantiene el máximo de 40% de descuento acumulado.
#________________________________________
#Condición especial
#La universidad quiere premiar especialmente a los estudiantes con buen rendimiento.
#Si:
#NEM >= 6.5
#Y
#tiene beca
#el estudiante recibe un mensaje especial:
