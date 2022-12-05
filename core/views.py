from django.shortcuts import render
from django.http import HttpResponse

from catalogo.models import Categoria

def index(request):
   
    texts =['TEste de texto','teste2 de texto']
    context = {
        'title': 'página trilha_back',
        'texts': texts,
        
    }
    return render(request,'index.html', context)

def contato(request):
    return render (request, 'contato.html')

def produto(request):
    return render (request, 'produtos.html')