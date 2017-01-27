import random
def crear_archivo(password):
	file = open("archivo.txt", "w")
	file.close()

def crear_contra(cant, longi, letras):
	contraseñas= []

	for i in range(cant):
		contra_final= []
		random.shuffle(letras)
		for i in range(longi):
			contra_final.append(letras[i])
			contraseñas.append(contra_final)

	return contraseñas