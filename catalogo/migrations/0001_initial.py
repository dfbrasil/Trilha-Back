# Generated by Django 4.1 on 2022-12-05 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(blank=True, max_length=100, verbose_name='Indentificador')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em: ')),
            ],
            options={
                'verbose_name': ('Categoria',),
                'verbose_name_plural': ('Categorias',),
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(blank=True, max_length=100, verbose_name='Indentificador')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição: ')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Preço: ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em: ')),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalogo.categoria', verbose_name='Categoria: ')),
            ],
            options={
                'verbose_name': ('Produto',),
                'verbose_name_plural': ('Produtos',),
                'ordering': ['name'],
            },
        ),
    ]
