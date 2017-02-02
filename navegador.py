class Navegador(object):
	def __init__ (self, nombre, version ):
		self.tabs=[]
		self.nombre = nombre
		self.version = version


	def agregar_tabs(self, tab):
		self.tabs.append(tab)



	def cerrar_tabs(self, n, tabs):
		n-= 1
		self.tabs.pop(n)



	def cerrar_todas(self, tabs):
		self.tabs=[]


	def mostrar_tabas(self, tabs):
		for i in range(0, len(self.tabs)):
			return self.tabs[i]


	def guardar_tabas(self, tabs):









		