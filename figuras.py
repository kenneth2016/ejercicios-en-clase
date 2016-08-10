from cuadrado import Cuadrado
from triangulo import Triangulo

figura =None
print ("1.crear figura \n 2.salir")

opc=int(input("ingrese una opcion: "))

while opc!= 2:
	if opc==1:
		fig= int(input("1.cuadrado , 2.triangulo: "))
		