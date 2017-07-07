#python /../../../BlackBell/challenges3.py
from fun import *


def start():
	print("comenzamos el juego elige el tamaño del escenario")
	res=False
	#checa si el tamaño es un int, si no mueres
	#crea la pista
	while (res ==False):
		tam=input()
		if tryCatch(tam):			
			res=pista(int(tam),1)
		else:
			salida()
	#
	while (res ==True):
		print('Elige una pos')
		pos=input()
		if type(pos) is str:
			if pos == "exit":
				salida()
			else:
				pista(int(tam),pos)
		elif type(pos) is int:
			if int(pos)<tam*tam:
				pista(tam,pos)
			else:
				print('no te pases')
		else:
			print('Eso no sirve')
		

start()