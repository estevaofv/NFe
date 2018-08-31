from django.contrib import admin
from models import Nota, Produto

modelos = [Nota, Produto]
admin.site.register(modelos)
