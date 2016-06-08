opc= int(input("elija una opcion: \n 1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4.salir \n: "))
students={}
while opc!=4:
	if opc == 1:
		nom=input("ingrese el nombre del estudiante: ")
		students[nom]=[]
		print (students)
	opc= int(input("elija una opcion: \n 1.crear estudiante \n 2.ingresar notas \n 3.reporte de notas \n 4.salir \n: "))
	if opc == 2:
		estu = input("a que estudiante quiere agregar una nota: ")
		nota int(input("ingrese la nota: "))