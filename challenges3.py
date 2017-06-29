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
		pos=input()
		if pos == "exit":
			print(""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .
                              :
                              "".")""")
		if int(pos)<tam*tam:
			pista(tam,pos)
		else:
			print('no te pases')
		

start()