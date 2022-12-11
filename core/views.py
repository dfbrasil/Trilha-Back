from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContatoForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')


def my_logout(request):
    logout(request)
    return redirect('index')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})


def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucesso = True
    context = {
        'form' : form,
        'sucesso' : sucesso
    }
    return render (request, 'contato.html', context)



