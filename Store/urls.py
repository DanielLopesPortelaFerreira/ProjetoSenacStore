
from Store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('departamentos/', views.departamentos, name = 'departamentos'),
    path('categorias/', views.categoria, name = 'categorias'), # "name" é relativo ao endereço de "http"
    path('produtos/', views.produtos, name = 'produtos')
]