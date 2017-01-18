def notas_pro (n):
	promedio=0
	for i in range(0,len(n)):
		promedio+= n[i]
	return (promedio/len(n))