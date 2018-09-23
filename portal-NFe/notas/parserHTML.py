import bs4
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import re
import json

#Abertura do arquivo HTML, teste estático
doc = urlopen('https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?chNFe=43180387397865001940652080000042681261512136&').read()
doc = doc.decode('utf-8')
if doc == "":
    sys.exit()

#Criação do BeatifulSoup object, formata o HTML
soup = BeautifulSoup(doc, 'html.parser')

#Pega o link onde estão os arquivos de notas fiscais
link = soup.iframe['src']
print (link)

#Abertura do arquivo HTML obtido acima
doc = urlopen(link).read()
if doc == "":
    sys.exit()
doc = doc.decode('iso-8859-1')

#Criação do BS object
soup = BeautifulSoup(doc, 'html.parser')

#Encontra o conteúdo das tags que contém o nome do produto, sobrescrita proposital
count = 0
try:
    for tag in soup.find_all('td', class_='NFCDetalhe_Item', style='width: 300px;'):
        product = tag.string
        print(product)
except:
    e = sys.exc_info()[0]
    print('Error founded', e)

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

for tag in soup.find('td', class_='NFCCabecalho_SubTitulo1'):
    list = tag.string
    cnpj = list[55:72]
    print('CNPJ: ', cnpj)
    