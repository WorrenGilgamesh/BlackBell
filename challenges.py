esc = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

def creaEsc(tam,esc):
	for x in esc:
		if x%tam==0:
			print x
		else:
			print x," ",
def arreEsc(tam):
	arre=[]
	for y in xrange(1,tam+1):
		for x in xrange(1,tam+1):
			arre.append(x)
	return(arre)
def juego(var):
	creaEsc(var,arreEsc(var))

juego(5)
#arreEsc(5)
