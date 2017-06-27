import math
def digitos(tam,esc):
	len(str(123))
	t=()
	for x in esc:
		t=t+(x,)
	return t
def creaEsc(tam,esc):
	for x in esc:
		if x%tam==0:
			print('{:>4}'.format(x))
		else:
			print('{:>4}'.format(x), end=' ')

def arreEsc(tam):
	arre=[]
	#for y in range(1,tam+1):
	for x in range(1,tam+1):
		arre.append(x)
	return(arre)

def juego(var):
	var=var*var
	creaEsc(var/math.sqrt(var),arreEsc(var))

juego(45)