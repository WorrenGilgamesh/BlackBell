#python /../../../BlackBell/challenges3.py
import math
def digitos(tam,esc):
	len(str(123))
	t=()
	for x in esc:
		t=t+(x,)
	return t
def jugador(posicion):
	return posicion
def creaEsc(tam,esc,jugadorPos):
	for x in esc:
		if x%tam==0:
			if jugador(jugadorPos)==x:
				print('{:>4}'.format('a'))
			else:
				print('{:>4}'.format(x))
			print(' ')
		else:
			if jugador(jugadorPos)==x:
				print('{:>4}'.format('a'), end=' ')
			else:
				print('{:>4}'.format(x), end=' ')
def arreEsc(tam):
	arre=[]
	#for y in range(1,tam+1):
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
def start():
	print("comenzamos el juego elige el tamaño del escenario")
	res=False
	while (res ==False):
		tam=int(input())
		res=pista(tam,1)
	while (res ==True):
		print('Elige una pos')
		pista(tam,int(input()))

start()