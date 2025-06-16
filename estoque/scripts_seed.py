# -*- coding: utf-8 -*-
from estoque.models import Fornecedor, Deposito, Produto

# Fornecedores
f1 = Fornecedor.objects.create(nome="Água Boa", telefone="11999999999", endereco="Rua das Águas, 100", responsavel="João")
f2 = Fornecedor.objects.create(nome="Gás Total", telefone="11888888888", endereco="Av. do Gás, 200", responsavel="Maria")

# Depósitos
d1 = Deposito.objects.create(descricao="Depósito Central", endereco="Rua Central, 123")

# Produtos
Produto.objects.create(descricao="Água Mineral 20L", unidade="lt", fornecedor=f1, deposito_padrao=d1)
Produto.objects.create(descricao="Gás GLP 13kg", unidade="kg", fornecedor=f2, deposito_padrao=d1)
Produto.objects.create(descricao="Água Mineral 10L", unidade="lt", fornecedor=f1, deposito_padrao=d1)
Produto.objects.create(descricao="Gás GLP 45kg", unidade="kg", fornecedor=f2, deposito_padrao=d1)

print('Dados fictícios cadastrados com sucesso!') 