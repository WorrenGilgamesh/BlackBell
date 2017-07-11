from prints import *
import math
conta=1
def jugador(posicion,tam):
    return {
    	'cero':conta,
    	'der':der(tam),
    	'aba':aba(tam),
    	'izq':izq(tam),
    	'arr':arr(tam),
    }.get(posicion, 0)

def der(tam):
	res=int(conta+1)
	return res
def aba(tam):
	res=int(tam+conta)
	return res
def izq(tam):
	res=int(conta-1)
	return res
def arr(tam):
	res=int(conta-tam)
	return res

def creaEsc(tam,esc,jugadorPos):
	global conta
	print(conta)
	if conta>0 and conta<tam*tam:
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
		conta=jugador(jugadorPos,tam)
	else:
		salida()

def arreEsc(tam):
	arre=[]
	for x in range(1,tam+1):
		arre.append(x)
	return(arre)

#En primer instancia le pasa al jugado en pos 1
#var es el tamaño de las pista
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
