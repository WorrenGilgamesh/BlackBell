from prints import *
import math
def digitos(tam,esc):
	len(str(123))
	t=()
	for x in esc:
		t=t+(x,)
	return t

def jugador(posicion,tam):
    return {
    	'arriba':1 ,
    	'abajo': 2,
    }.get(posicion, 0)

def creaEsc(tam,esc,jugadorPos):
	for x in esc:
		if x%tam==0:
			if jugador(jugadorPos,tam)==x:
				print('{:>4}'.format('a'))
			else:
				print('{:>4}'.format(x))
			print(' ')
		else:
			if jugador(jugadorPos,tam)==x:
				print('{:>4}'.format('a'), end=' ')
			else:
				print('{:>4}'.format(x), end=' ')

def arreEsc(tam):
	arre=[]
	for x in range(1,tam+1):
		arre.append(x)
	return(arre)

def pista(var,jugadorPos):
	if var<=16:
		var=var*var
		creaEsc(var/math.sqrt(var),arreEsc(var),jugadorPos)
		return True
	else:
		print("Un numero del 1 al 16")
		return False
def tryCatch(x):
    try:
        int(x) is int
        return True
    except Exception:
        print("Eso no sirve")
    return False
def salida():
	muerte()
	print(' ')
	gameOver()
	exit()
