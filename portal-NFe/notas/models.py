from django.db import models

class Estabelecimento(models.Model):
    cnpj   = models.CharField('CNPJ',   max_length=18, blank=False, unique=True)
    nome   = models.CharField('Nome',   max_length=40, blank=False)
    email  = models.EmailField('Email', max_length=40, blank=False)
    rua    = models.CharField('Rua',    max_length=40, blank=False)
    numero = models.CharField('Número', max_length=40, blank=False)
    bairro = models.CharField('Bairro', max_length=40, blank=False)
    cep    = models.CharField('CEP',    max_length=9,  blank=False)
    cidade = models.CharField('Cidade', max_length=40, blank=False)
    uf     = models.CharField('Estado', max_length=40, blank=False)

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['cnpj']

    def __str__(self):
        return self.cnpj

class Nota(models.Model):
    chave  = models.CharField('Chave de Acesso', max_length=44, unique=True)
    numero = models.CharField('Número da NF-e', max_length=9)
    data   = models.DateField('Data de Emissão')
    xml    = models.BinaryField('XML NF-e', blank=True)
    cnpj   = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['data']

    def __str__(self):
        return self.chave

class Produto(models.Model):
    codigo = models.CharField('Codigo', max_length=20, unique=True)
    nome   = models.CharField('Nome',   max_length=40)
    preco  = models.FloatField('Preço')
    nota   = models.ForeignKey(Nota, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.codigo