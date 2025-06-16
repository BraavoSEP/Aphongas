# Aphongas

Sistema de controle de estoque para pequenas empresas de distribuição de água, gás e similares.

## Funcionalidades
- Cadastro e pesquisa de produtos
- Cadastro e pesquisa de depósitos
- Cadastro e pesquisa de fornecedores
- Cadastro e pesquisa de usuários (apenas administradores)
- Autenticação de usuários (login/logout)
- Movimentação de produtos (entrada e saída)
- Relatório de estoque (entradas, saídas e saldo)

## Tecnologias Utilizadas
- Python 3
- Django

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/BraavoSEP/Aphongas.git
   cd Aphongas
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências:**
   ```bash
   pip install django
   ```

4. **Realize as migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema:**
   - Abra o navegador e acesse: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

## Estrutura das Telas
- **Produtos:** Cadastro, pesquisa, seleção de fornecedor e depósito padrão.
- **Depósitos:** Cadastro e pesquisa.
- **Fornecedores:** Cadastro e pesquisa.
- **Usuários:** Cadastro e pesquisa (apenas para administradores).
- **Movimentação:** Cadastro de entrada e saída de produtos, validação de estoque.
- **Relatório:** Tabela com entradas, saídas e saldo de cada produto.

## Observações
- Apenas administradores podem cadastrar novos usuários.
- O sistema utiliza autenticação padrão do Django.
- O layout utiliza Bootstrap para responsividade e facilidade de uso.

## Licença
Este projeto é apenas para fins acadêmicos e de demonstração. 