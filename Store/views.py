from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import context
from Store.models import Departamento, Categoria, Produto

# Create your views here.
def index(request):
    meu_nome = 'Daniel en teste'
    sexo = 'M'
    context = {'nome': meu_nome, 'artigo': 'o' if sexo == 'M' else 'a'}

    return render(request,'index.html', context)

def teste(request):
    # depto = ['Casa', 'Informática', 'Telefonia']
    depto = Departamento.objects.all()
    context = {'departamentos': depto } 
    return render(request, 'teste.html', context)

def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos': depto } 
    return render(request, 'Departamentos.html', context)

def categoria(request, id):
    cat = Categoria.objects.filter(departamento_id = id)
    context = {'categorias': cat } 
    return render(request, 'Categorias.html', context)

def produtos(request, id):
    pdt = Produto.objects.filter(categoria_id = id)
    context = {'produtos': pdt}
    return render(request, 'produtos.html', context)