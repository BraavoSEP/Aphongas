from .models import Fornecedor, Deposito, Produto, Usuario, Movimentacao
from django.contrib import admin

# Register your models here.

admin.site.register(Fornecedor)
admin.site.register(Deposito)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Movimentacao)
