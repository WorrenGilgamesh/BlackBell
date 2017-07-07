#https://www.dataquest.io/blog/web-scraping-tutorial-python/
#http://liceu.uab.cat/~joaquim/language_technology/NLP/PLN_analisis.html
#https://foro.elhacker.net/scripting/busqueda_en_la_rae_raepy-t289342.0.html	
#http://lexicoon.org
#http://www.eldiario.es/hojaderouter/tecnologia/software/lenguajes_de_programacion-gobernanza-comunidad-responsables_0_478402349.html
import requests
from bs4 import BeautifulSoup
page = requests.get("http://dle.rae.es/?w=KYtLWBc")
#print(page)
#print(page.status_code)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
soup =soup.prettify()
list(soup.children)
[type(item) for item in list(soup.children)] 
html = list(soup.children)[2]
list(html.children)