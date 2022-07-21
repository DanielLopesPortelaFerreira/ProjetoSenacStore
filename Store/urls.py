
from Store import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste')
]