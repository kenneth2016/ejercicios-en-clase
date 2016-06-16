from collections import deque
def es_palindromo(f):
	pila=[]
	cola=deque([])
	for letra in f:
		pila.append(letra)
		cola.append(letra)
	for i in range(len(f)):
		if cola.popleft() != pila.pop():
			return False

	return True


