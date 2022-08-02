
from Store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    path('departamentos/', views.departamentos, name = 'departamentos'),
    path('categorias/<int:id>', views.categoria, name = 'categorias'), # "name" é relativo ao endereço de "http"
    path('produtos/<int:id>', views.produtos, name = 'produtos')
]