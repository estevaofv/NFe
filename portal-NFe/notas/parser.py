import bs4
import urllib
import re
import json
import sys

from bs4 import BeautifulSoup
from urllib.request import urlopen

def getEmpresa(cnpj):

    cnpj_clean = str(cnpj)
    cnpj_clean = cnpj_clean.replace('.', '')
    cnpj_clean = cnpj_clean.replace('/', '')
    cnpj_clean = cnpj_clean.replace('-', '')
    cnpj_clean = cnpj_clean.replace(' ', '')

    link = 'http://receitaws.com.br/v1/cnpj/' + cnpj_clean

    info = json.loads(urlopen(link).read().decode('utf-8'))

    empresa = {}
    empresa['nome']      = info['fantasia']
    empresa['cnpj']      = info['cnpj']
    empresa['telefone']  = info['telefone']
    empresa['email']     = info['email']
    empresa['bairro']    = info['bairro']
    empresa['rua']       = info['logradouro']
    empresa['numero']    = info['numero']
    empresa['cep']       = info['cep']
    empresa['municipio'] = info['municipio']
    empresa['estado']    = info['uf']

    return  empresa


def getProdutosComQRCode(url):
    link = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser').iframe['src']
    doc = urlopen(link).read().decode('iso-8859-1')
    if doc == "":
        sys.exit()
    soup = BeautifulSoup(doc, 'html.parser')

    data = {}

    try:
        cnpj = soup.find('td', class_='NFCCabecalho_SubTitulo1').string[55:73]
        data['empresa'] =    getEmpresa(cnpj)

        data['produtos'] = {}

        for tag in soup.find_all('tr', id=re.compile("Item +")):
            produto = []
            for child in tag.find_all('td', class_='NFCDetalhe_Item'):
                produto.append(child.string)
            data['produtos'][tag['id']] = produto

        return data
    except:
        e = sys.exc_info()[0]
        print('Error founded', e)
