import requests
from bs4 import BeautifulSoup
import codecs
import time



#Porcesador de lemario
#procesador web para sacar palabra, significado, ejemplo, separacion
#===================================================================================================
#===================================================================================================
def palabra(line):
	sign=""
	page = requests.get("http://acepciones.com/"+line+"/")
	soup = BeautifulSoup(page.content, 'html.parser')
	count=0
	for x in soup.find_all('tr'):
		sign+=soup.find_all('tr')[count].get_text()
		count +=1
	return sign
#===================================================================================================
#===================================================================================================

def diccionario():
	with codecs.open('lemari.txt',encoding='utf-8') as fin:
		for line in fin:			
			print(palabra(line))

diccionario()