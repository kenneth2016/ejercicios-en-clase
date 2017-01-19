from notas import notas_pro
print ("Bienvenidos")
seguir = input("desea iniciar? 1.si o 2.no?: ")
n =[]
while seguir == "1":
	nota =int(input("ingrese una nota: "))
	while nota<0 or nota>100:
		nota=int(input("ingrese una nota valida: "))
	n.append(nota)
	seguir = input("desea seguir? 1.si o 2.no?: ")

print(notas_pro(n))