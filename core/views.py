from django.shortcuts import render
from django.http import HttpResponse

from catalogo.models import Categoria
from .forms import ContatoForm

from django.views.generic import View, TemplateView

from django.core.mail import send_mail

class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()


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



