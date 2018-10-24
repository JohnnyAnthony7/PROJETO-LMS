from django.shortcuts import render
from django.views.generic import CreateView, ListView


def home(request):
        return render(request,'index.html')

def listaCurso(request):
        return render(request, 'ListadeCursos.html')

def detalhesCurso(request):
        return render(request, 'DetalhesdeCurso.html')

def login(request):
        return render(request, 'Login.html')

def noticias(request):
        return render(request, 'Noticias.html')

def disciplinas(request):
        return render(request, 'Disciplinas.html')

def esqueceuSenha(request):
    return render(request, 'Esqueceusenha.html')


