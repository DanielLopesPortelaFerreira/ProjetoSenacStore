from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello Word!')

def teste(request):
    return HttpResponse('Minha página de teste')