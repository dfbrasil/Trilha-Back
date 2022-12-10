from django.urls import path

from . import views

urlpatterns = [

    path('', views.produtos_list, name='produtos_list'),
    path('<slug>/', views.categoria, name='categoria'),
    path('produtos/<slug>/', views.produto, name='produto'),

]
