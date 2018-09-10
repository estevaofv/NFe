import html.parser
from html.parser import HTMLParser
import urllib
from urllib.request import urlopen

page = '\''
site = ''
inTag = False
areItem = False

class ParserNotas(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'iframe':
			for names, value in attrs:
				if names == 'src':
					site = page + value + page
					print (site)


		if tag == 'td':
			for names, value in attrs:
				if names == 'class' and value == 'NFCDetalhe_Item':
					areItem = True
					#print ('achei')
				if names == 'style' and value == 'width: 300px;' and areItem:	
					inTag = True
					print ('achei o item') #Como pegar o conteúdo da Tag?

	def handle_endtag(self, tag):
		if tag == 'iframe':
			print('fechou a tag: ', tag)

	def handle_data(self, data):
		if inTag:
			print (data)
		
p = ParserNotas()
doc = urlopen('https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?chNFe=43180387397865001940652080000042681261512136&').read()
p.feed(doc.decode('utf-8'))

#print ('aaa', site) #não tá mostrando o site?
pageNFe = ParserNotas()
doc = urlopen('https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_QRCODE_1.asp?chNFe=43180387397865001940652080000042681261512136&').read()
pageNFe.feed(doc.decode('iso-8859-1'))
