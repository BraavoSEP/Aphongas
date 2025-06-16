from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .models import Fornecedor, Deposito, Produto, Usuario, Movimentacao
from .forms import FornecedorForm, DepositoForm, ProdutoForm, UsuarioForm, UsuarioPerfilForm, MovimentacaoForm
from django.contrib.auth.models import User
from django.db.models import Sum, Q

# Função para verificar se o usuário é admin

def is_admin(user):
    try:
        return user.usuario.eh_admin
    except:
        return False

# Cadastro e pesquisa de fornecedores
@login_required
def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'estoque/fornecedores.html', {'fornecedores': fornecedores, 'form': form})

# Cadastro e pesquisa de depósitos
@login_required
def depositos(request):
    depositos = Deposito.objects.all()
    if request.method == 'POST':
        form = DepositoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depositos')
    else:
        form = DepositoForm()
    return render(request, 'estoque/depositos.html', {'depositos': depositos, 'form': form})

# Cadastro e pesquisa de produtos
@login_required
def produtos(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/produtos.html', {'produtos': produtos, 'form': form})

# Cadastro e pesquisa de usuários (apenas admin)
@login_required
@user_passes_test(is_admin)
def usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        perfil_form = UsuarioPerfilForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            perfil = perfil_form.save(commit=False)
            perfil.user = user
            perfil.save()
            return redirect('usuarios')
    else:
        user_form = UsuarioForm()
        perfil_form = UsuarioPerfilForm()
    return render(request, 'estoque/usuarios.html', {'usuarios': usuarios, 'user_form': user_form, 'perfil_form': perfil_form})

# Cadastro de movimentação
@login_required
def movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            mov = form.save(commit=False)
            # Verifica se é saída e se há estoque suficiente
            if mov.tipo == 'S':
                total_entrada = Movimentacao.objects.filter(produto=mov.produto, tipo='E').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
                total_saida = Movimentacao.objects.filter(produto=mov.produto, tipo='S').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
                saldo = total_entrada - total_saida
                if mov.quantidade > saldo:
                    form.add_error('quantidade', 'Quantidade insuficiente em estoque!')
                    return render(request, 'estoque/movimentacao.html', {'form': form})
            mov.usuario = request.user
            mov.save()
            return redirect('movimentacao')
    else:
        form = MovimentacaoForm()
    return render(request, 'estoque/movimentacao.html', {'form': form})

# Relatório de estoque
@login_required
def relatorio_estoque(request):
    produtos = Produto.objects.all()
    relatorio = []
    for produto in produtos:
        entrada = Movimentacao.objects.filter(produto=produto, tipo='E').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
        saida = Movimentacao.objects.filter(produto=produto, tipo='S').aggregate(Sum('quantidade'))['quantidade__sum'] or 0
        saldo = entrada - saida
        relatorio.append({
            'produto': produto,
            'entrada': entrada,
            'saida': saida,
            'saldo': saldo
        })
    return render(request, 'estoque/relatorio.html', {'relatorio': relatorio})

# Autenticação
from django.contrib.auth.views import LoginView, LogoutView
