from django.shortcuts import render
from django.http import HttpResponse

from catalogo.models import Categoria
from .forms import ContatoForm

from django.core.mail import send_mail



def index(request):
   
    texts =['TEste de texto','teste2 de texto']
    context = {
        'title': 'página trilha_back',
        'texts': texts,
        
    }
    return render(request,'index.html', context)

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



