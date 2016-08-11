from cuadrado import Cuadrado
from triangulo import Triangulo

figura =None
print ("1.crear figura \n 2.salir")

opc1=int(input("ingrese una opcion: "))
opc2=None

while opc2!=4:
	if opc1==1 or opc2==2:
		fig=int(input(" elija una figura: \n 1. cuadrado \n 2. triangulo: "))
		if fig == 2:
			altura= int(input("ingrese la altura: "))
			base = int(input("ingrese la base: "))
			figura=Triangulo (base, altura)

		if fig == 1:
			lado = int(input("ingrese el lado: "))
			figura= Cuadrado(lado)

	if opc2==2:
		print("area: " , figura.calcular_area())

	if opc2==3:
		print ("figura: ", figura.imprimir())

	print("1.crear figura\n 2.mostrar area\n 3.imprimir\n 4.salir")
	opc2=int(input("elija la opcion que desea: "))




