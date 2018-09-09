from django.contrib import admin
from models import Nota, Produto, Supermercado

modelos = [Nota, Produto, Supermercado]
admin.site.register(modelos)
