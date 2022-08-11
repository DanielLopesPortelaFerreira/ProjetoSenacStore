from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import context
from Store.models import Departamento, Categoria, Produto
from django.core.mail import send_mail

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
    depto = Departamento.objects.get(id = id)
    context = {
        'categorias': cat,
        'departamento': depto
        } 
    return render(request, 'Categorias.html', context)

def produtos(request, id):
    pdt = Produto.objects.filter(categoria_id = id)
    categ = Categoria.objects.get(id = id)
    context = {
        'produtos': pdt,
        'categorias': categ
        }
    return render(request, 'produtos.html', context)

def produto_detalhe(request, id): #linha de nome pagina html
    pdt_de = Produto.objects.get(id = id) # variável que em conjunto com o model "Produto" e comando ".objects.get ou objects.filter" faz uma busca no banco de dados
    context = { 'prod': pdt_de} #variavel de contexto: retorno de informações
    return render(request, 'Produto_Detalhe.html', context)

def institucional(request):
    return render(request, 'institucional.html')

def contato(request):
    return render(request, 'Contato.html')

def enviar_email(request):
    nome= request.POST['nome']
    telefone= request.POST['telefone']
    assunto= request.POST['assunto']
    mensagem= request.POST['mensagem']
    remetente= request.POST['email']
    destinatario= ['androidanny274@gmail.com']
    corpo= f"Nome: {nome}  \n Telefone: {telefone} \n Mensagem: {mensagem}"

    try:
        send_mail(assunto, corpo, remetente, destinatario)
        context = {'msg': 'E-mail enviado com sucesso'}

    except:
        context = {'msg': 'Erro ao enviar E-mail'}

    return render(request, 'contato.html', context)