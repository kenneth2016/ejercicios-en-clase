from notas import notas_pro
print ("Bienvenidos")
seguir = input("desea iniciar? 1.si o 2.no?: ")
n =[]
while seguir == "1":
	nota =int(input("ingrese una nota: "))
	if nota>0 and nota<=100