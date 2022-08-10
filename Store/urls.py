
from Store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('departamentos/', views.departamentos, name = 'departamentos'),
    path('categorias/<int:id>', views.categoria, name = 'categorias'), # "name" é relativo ao endereço de "http"
    path('produtos/<int:id>', views.produtos, name = 'produtos'),
    path('produto_detalhe/<int:id>', views.produto_detalhe, name = 'Produto_Detalhe'),
    path('institucional/', views.institucional, name='institucional'),
    path('Contato/',views.contato, name= 'Contato')
]