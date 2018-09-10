from django.contrib import admin
from .models import Nota, Produto, Estabelecimento

class NotaAdmin(admin.ModelAdmin):
    #list_display = ['cnpj', 'rua', 'numero', 'bairro', 'cep', 'cidade', 'uf']
    search_fields = []
    list_filter = []

class ProdutoAdmin(admin.ModelAdmin):
    #list_display = ['chave', 'numero', 'data', 'xml']
    search_fields = []
    list_filter = []

class EstabelecimentoAdmin(admin.ModelAdmin):
    #list_display = ['codigo', 'nome', 'preco']
    search_fields = []
    list_filter = []

admin.site.register(Nota, NotaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
