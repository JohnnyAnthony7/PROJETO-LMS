from django.shortcuts import render
from django.views.generic import CreateView
from lms_app.models import *


def home(request):
        return render(request,'index.html')

def listaCurso(request):
        return render(request, 'ListadeCursos.html')

def login(request):
        return render(request, 'Login.html')

def disciplinas(request):
        return render(request, 'Disciplinas.html')

def esqueceuSenha(request):
    return render(request, 'Esqueceusenha.html')

def telaCadastros(request):
    return render(request,'cadastro.html')

class cadastroAluno(CreateView):
    template_name = 'cadastroAlunos.html'
    model = Aluno
    fields = "__all__"

class cadastroProfessor(CreateView):
    template_name = 'cadastroProfessores.html'
    model = Professor
    fields = "__all__"

class cadastroDisciplina(CreateView):
    template_name = 'cadastroDisciplinas.html'
    model = Disciplina
    fields = "__all__"

def cursoADM(request):
        return render(request, 'adm.html')

def cursoBD(request):
        return render(request, 'bd.html')

def cursoADS(request):
        return render(request, 'ads.html')

def cursoADSEAD(request):
        return render(request, 'adsead.html')

def cursoEngenharia(request):
        return render(request, 'engenharia.html')

def cursoProcessos(request):
        return render(request, 'processos.html')

def cursoSI(request):
        return render(request, 'si.html')

def cursoJogos(request):
        return render(request, 'jogos.html')

def cursoGestao(request):
        return render(request, 'gestao.html')

def cursoRedes(request):
        return render(request, 'redes.html')

def cursoProducao(request):
        return render(request, 'producao.html')