import requests
from bs4 import BeautifulSoup
import codecs

#Porcesador de lemario
#procesador web para sacar palabra, significado, ejemplo, separacion
#===================================================================================================
#===================================================================================================
def palabra():
	with codecs.open('lemari.txt',encoding='utf-8') as fin:
		for line in fin:
			page = requests.get("http://acepciones.com/"+line+"/")
			soup = BeautifulSoup(page.content, 'html.parser')
			count=0
			for x in soup.find_all('tr'):
				print(soup.find_all('tr')[count].get_text())
				count +=1
#===================================================================================================
#===================================================================================================

palabra()