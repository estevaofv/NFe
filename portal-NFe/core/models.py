from django.db import models


class Nota(models.Model):
    codigo = models.CharField(max_length=20)
    num_produtos = models.DecimalField(max_digits=5)


class Produto(models.Model):
    descricao = models.TextField
