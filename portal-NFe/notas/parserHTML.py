import bs4
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import re

#Abertura do arquivo HTML, teste estático
doc = urlopen('https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?chNFe=43180387397865001940652080000042681261512136&').read()
doc = doc.decode('utf-8')

#Criação do BeatifulSoup object, formata o HTML
soup = BeautifulSoup(doc, 'html.parser')

#Pega o link onde estão os arquivos de notas fiscais
link = soup.iframe['src']

#Abertura do arquivo HTML obtido acima
doc = urlopen(link).read()
doc = doc.decode('iso-8859-1')

#Criação do BS object
soup = BeautifulSoup(doc, 'html.parser')

#Encontra o conteúdo das tags que contém o nome do produto, sobrescrita proposital
count = 0
for tag in soup.find_all('td', class_='NFCDetalhe_Item', style='width: 300px;'):
	product = tag.string
	sprint(product)

#Encontra o preço de cada produto especificado na nota, sobrescrita proposital
for tag in soup.find_all('tr', id=re.compile("Item +")):
	for child in tag.find_all('td', class_='NFCDetalhe_Item', style='width: 70px;'):
		count = count + 1
		if (count % 2 == 1):
			price = child.string
			print(price)

for father in soup.find_all('tr', id=re.compile("Item +")):
    for tag in father.find_all('td', class_='NFCDetalhe_Item', style='width: 60px;'):
        code = tag.string
        print(code)

for father in soup.find_all('tr', id=re.compile("Item +")):
    for tag in father.find_all('td', class_='NFCDetalhe_Item', style='width: 10px;'):
        unity = tag.string
        print(unity)

def getProducts(chave):
    url = "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?chNFe=" + chave + "&"
    doc = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(doc, 'html.parser')
    link = soup.iframe['src']
    doc = urlopen(link).read().decode('iso-8859-1')
    soup = BeautifulSoup(doc, 'html.parser')

    for tag in soup.find_all('tr', id=re.compile("Item +")):
        for child in tag.find_all('td', class_='NFCDetalhe_Item'):
            print (child)
    



    
    return