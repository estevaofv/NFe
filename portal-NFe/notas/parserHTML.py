import html.parser
from html.parser import HTMLParser
import urllib
from urllib.request import urlopen

page = '\''

class ParserNotas(HTMLParser):
	site = ''
	inTag = False
	areItem = False

	def handle_starttag(self, tag, attrs):
		if tag == 'iframe':
			for names, value in attrs:
				if names == 'src':
					self.site = page + value + page
					#print (self.site)


		if tag == 'td':
			for names, value in attrs:
				if names == 'class' and value == 'NFCDetalhe_Item':
					self.areItem = True
					#print ('achei')
				if names == 'style' and value == 'width: 300px;' and self.areItem:	
					self.inTag = True
					print ('achei o item') #Como pegar o conteúdo da Tag?

	def handle_endtag(self, tag):
		if tag == 'td':
			self.inTag = False

	def handle_data(self, data):
		if self.inTag:
			print (data)
		
p = ParserNotas()
doc = urlopen('https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?chNFe=43180387397865001940652080000042681261512136&').read()
p.feed(doc.decode('utf-8'))

pageNFe = ParserNotas()
doc = urlopen('https://www.sefaz.rs.gov.br/ASP/AAE_ROOT/NFE/SAT-WEB-NFE-NFC_QRCODE_1.asp?chNFe=43180387397865001940652080000042681261512136&').read()
pageNFe.feed(doc.decode('iso-8859-1'))
