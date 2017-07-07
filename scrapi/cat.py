import requests
from bs4 import BeautifulSoup

page = requests.get("http://acepciones.com/hola/")
soup = BeautifulSoup(page.content, 'html.parser')
count=0
for x in soup.find_all('tr'):
	print(soup.find_all('tr')[count].get_text())
	count +=1
