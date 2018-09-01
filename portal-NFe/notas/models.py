from django.db import models

class Estabelecimento(models.Model):
    cnpj   = models.CharField('CNPJ',   max_length=18, blank=False, unique=True)
    rua    = models.CharField('Rua',    max_length=40, blank=False)
    numero = models.CharField('Número', max_length=40, blank=False)
    bairro = models.CharField('Bairro', max_length=40, blank=False)
    cep    = models.CharField('CEP',    max_length=9,  blank=False)
    cidade = models.CharField('Cidade', max_length=40, blank=False)
    uf     = models.CharField('Estado', max_length=40, blank=False)

class Nota(models.Model):
    chave  = models.CharField('Chave de Acesso', max_length=44, unique=True)
    numero = models.CharField('Número da NF-e', max_length=9)
    data   = models.DateField('Data de Emissão')
    xml    = models.BinaryField('XML NF-e', blank=True)
    cnpj   = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

class Produto(models.Model):
    codigo = models.CharField('Codigo', max_length=20, unique=True)
    nome   = models.CharField('Nome',   max_length=40)
    preco  = models.FloatField('Preço')
    nota   = models.ForeignKey(Nota, on_delete=models.CASCADE)

