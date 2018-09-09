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



#class Nota(models.Model):
#    cod_nota = models.CharField(max_length=20)
#    chave_acesso = models.charField(max_length=50)
#    num_produtos = models.DecimalField(max_digits=5)
#    lista_produtos = models.DecimalField #Pensando em como adaptar pra pegar tudo da classe produto
    #data_emissao?
    #hora_emissao?


#class Produto(models.Model):
#    cod_prod = models.CharField(max_length=20)
#    descricao_prod = models.TextField
#    valor_un = models.FloatField
    #Aqui tentei pegar só o que a gente REALMENTE precisa, o resto acho que dá pra fazer quebrando XML

#class Supermercado(models.Model): #Pode futuramente virar 'estabelecimento' tendo uma variável 'tipo'
#    nome_super = models.CharField()
    #Endereço?
    #Contato?