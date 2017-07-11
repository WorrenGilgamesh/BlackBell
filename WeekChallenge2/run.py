import requests
from bs4 import BeautifulSoup
import codecs
import fileinput
import timeit
import os
import sys

#procesador web para sacar palabra, significado, ejemplo, separacion
#===================================================================================================
#===================================================================================================
def palabra(line):
	res=""
	page = requests.get("http://acepciones.com/"+line+"/")
	soup = BeautifulSoup(page.content, 'html.parser')
	count=0
	for x in soup.find_all('tr'):
		res+=soup.find_all('tr')[count].get_text()
		count +=1
	return res
#===================================================================================================
#===================================================================================================

#Porcesador de lemario y escritura de output
#===================================================================================================
#===================================================================================================

count =2896
def diccionario(cuenta):
	global count
	with codecs.open('lemarioEspanol.txt',encoding='utf-8') as fin:
		if count>0:
			for x in range(cuenta):
				fin.readline()		
		for line in fin:
			count+=1
			line=''.join(line.splitlines())
			sign=palabra(line)
			print(sign,file=open(line+".txt", "a"))
			#print(os.stat(line+".txt").st_size)
			if os.stat(line+".txt").st_size < 3:
				os.remove(line+".txt")
			else:
				for line in fileinput.FileInput(line+".txt",inplace=1):
					if line.rstrip():
						print(line)
			


#===================================================================================================
#==================================================================================================

def tryCatch():
    global count
    try:
        diccionario(count)
        return True
    except Exception:
        print("Error: ",count, sys.exc_info())
        count+=1
    return False

def measureTime():
	res=False
	start = timeit.timeit()
	while res == False:
		res=tryCatch()

	end = timeit.timeit()
	elapsed = end - start
	print("Time spent in (function name) is: ", elapsed)

measureTime()
#primera prueba Time spent in (function name) is:  0.0004042820044009715