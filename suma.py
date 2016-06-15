def suma (l):
	if len(l)==1:
		return l[0]

	subl = l[1:]
	submax= suma(subl)

	return submax + l[0]