from django.shortcuts import render

from .models import Produto, Categoria

def produtos_list(request):
    context = {
        'produtos_list': Produto.objects.all()
    }
    return render(request, 'catalogo/produtos_list.html', context)

def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    context = {
        'categoria_corrente':categoria,
        'produtos_list' : Produto.objects.filter(categoria=categoria),
    }
    return render(request, 'catalogo/categoria.html', context)