from django.shortcuts import render,get_object_or_404

from .models import Produto, Categoria

from django.views.generic import ListView
from django.core.paginator import Paginator

class ProdutosListView(ListView):

    model = Produto
    template_name = 'catalogo/produtos_list.html'
    context_object_name = 'produtos_list'
    paginate_by = 3

produtos_list = ProdutosListView.as_view()


class CategoriaListView(ListView):

    template_name = 'catalogo/categoria.html'
    context_object_name = 'produtos_list'
    paginate_by = 3

    def get_queryset(self):
        categoria = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return Produto.objects.filter(categoria = categoria)

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['categoria_corrente'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context

categoria = CategoriaListView.as_view()

# def categoria(request, slug):
#     categoria = Categoria.objects.get(slug=slug)
#     context = {
#         'categoria_corrente':categoria,
#         'produtos_list' : Produto.objects.filter(categoria=categoria),
#     }
#     return render(request, 'catalogo/categoria.html', context)


def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    context = {
        'produto' : produto
    }
    return render(request, 'catalogo/produto.html', context)