# -*- coding: utf-8 -*-
from estoque.models import Produto, Fornecedor, Deposito

Produto.objects.all().delete()
Fornecedor.objects.all().delete()
Deposito.objects.all().delete()

print('Produtos, fornecedores e depósitos apagados com sucesso!') 