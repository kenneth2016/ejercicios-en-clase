notas=[]
opc=input("desea ingresar una nota? si o no?: ")
while opc == "si":
	nota=str(input("ingrese la nota: "))
	notas.append(nota)
	opc=input("desea ingresar una nota? si o no?: ")

archi= open("notasguardadas.txt" , "w")
for nota in notas:
	archi.write(nota)
	archi.write("\n")
archi.close()

