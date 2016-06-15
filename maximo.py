def maximo (l):
	if len(l) ==1:
		return l[0]

	subl= l[1:]
	submax = maximo(subl)

	if l[0] > submax:
		return l[0]

	return submax