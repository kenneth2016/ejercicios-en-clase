print("Bienvenidos")
inventario={}
seguir= int(input("desea iniciar a ingresar porductos?: 1:si, 2:no : "))
while seguir == "1":
	item=input("ingrese su producto: ")
	print ("ingrese la cantidad de", item, ": ")
	cantidad= int(input())
	inventario[item]=cantidad
	seguir= int(input("desea ingresar otro producto?: 1:si 2:no :  "))
print (inventario)