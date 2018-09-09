from django.db import models


class Nota(models.Model):
    cod_nota = models.CharField(max_length=20)
    chave_acesso = models.charField(max_length=50)
    num_produtos = models.DecimalField(max_digits=5)
    lista_produtos = models.DecimalField #Pensando em como adaptar pra pegar tudo da classe produto
    #data_emissao?
    #hora_emissao?


class Produto(models.Model):
    cod_prod = models.CharField(max_length=20)
    descricao_prod = models.TextField
    valor_un = models.FloatField
    #Aqui tentei pegar só o que a gente REALMENTE precisa, o resto acho que dá pra fazer quebrando XML

class Supermercado(models.Model): #Pode futuramente virar 'estabelecimento' tendo uma variável 'tipo'
    nome_super = models.CharField()
    #Endereço?
    #Contato?