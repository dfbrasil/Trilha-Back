from django.contrib import admin

from .models import Produto,Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        # 'created'
        'modified'
    ]

    search_fields = [
        'name',
        'slug',
    ]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'categoria',
        # 'created'
        'modified'
    ]

    search_fields = [
        'name',
        'slug',
    ]

admin.site.register(Produto, ProdutoAdmin)

admin.site.register(Categoria, CategoriaAdmin)
