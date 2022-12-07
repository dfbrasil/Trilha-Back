from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    name = models.CharField(
        verbose_name='Nome',
        max_length=100,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name='Indentificador',
        max_length=100,
        blank=True,
    )

    created = models.DateTimeField(
        verbose_name='Criado em: ',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='Modificado em: ',
        auto_now=True,
    )

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return  reverse('catalogo:categoria', kwargs={'slug':self.slug})

    # class Meta:
    #     verbose_name = 'Categoria',
    #     verbose_name_plural = 'Categorias',
    #     ordering = ['name']


class Produto(models.Model):

    name = models.CharField(
        verbose_name='Nome',
        max_length=100,
        blank=True,
    )

    slug = models.SlugField(
        verbose_name='Indentificador',
        max_length=100,
        blank=True,
    )

    categoria = models.ForeignKey(
        'catalogo.Categoria',
        on_delete=models.DO_NOTHING,
        verbose_name='Categoria: ',
        blank=True,
    )

    descricao = models.TextField(
        verbose_name='Descrição: ',
        blank=True,
    )

    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Preço: ',
        blank=True, null= True,
    )

    created = models.DateTimeField(
        verbose_name='Criado em: ',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        verbose_name='Modificado em: ',
        auto_now=True,
    )

    def __str__(self):
        return self.name

    # class Meta:
    #     verbose_name = 'Produto',
    #     verbose_name_plural = 'Produtos',
    #     ordering = ['name']

    def get_absolute_url(self):
        return  reverse('catalogo:produto', kwargs={'slug':self.slug})