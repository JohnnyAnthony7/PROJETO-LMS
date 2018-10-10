from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def disciplinas(request):
    return render(request, 'Disciplinas.html')

def listaDeCursos(request):
    return render(request, 'ListadeCursos.html')

def login(request):
    return render(request, 'Login.html')

def noticias(request):
    return render(request, 'Noticias.html')

def detalhesDeCurso(request):
    return render (request, 'DetalhesdeCurso.html')

# Create your views here.
