from django import forms
from .models import Fornecedor, Deposito, Produto, Usuario, Movimentacao
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = '__all__'

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class UsuarioForm(UserCreationForm):
    eh_admin = forms.BooleanField(required=False, label='Administrador')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UsuarioPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['eh_admin']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = '__all__' 