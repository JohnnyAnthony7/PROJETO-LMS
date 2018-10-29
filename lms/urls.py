from lms_app import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^telaCadastro/$', views.telaCadastros, name='cadastro'),
    url(r'^cadastroAluno/$', views.cadastroAluno.as_view(), name='cadastroAluno'),
    url(r'^cadastroProfessor/$', views.cadastroProfessor.as_view(), name='cadastroProfessor'),
    url(r'^cadastroDisciplina/$', views.cadastroDisciplina.as_view(), name='cadastroDisciplina'),
    url(r'^cursoADM/$', views.cursoADM, name='ADM'),
    url(r'^cursoBD/$', views.cursoBD, name='BD'),
    url(r'^cursoADS/$', views.cursoADS, name='ADS'),
    url(r'^cursoADSEAD/$', views.cursoADSEAD, name='ADSEAD'),
    url(r'^cursoEngenharia/$', views.cursoEngenharia, name='Engenharia'),
    url(r'^cursoProcessos/$', views.cursoProcessos, name='Processos'),
    url(r'^cursoSI/$', views.cursoSI, name='SI'),
    url(r'^cursoJogos/$', views.cursoJogos, name='Jogos'),
    url(r'^cursoGestao/$', views.cursoGestao, name='Gestao'),
    url(r'^cursoRedes/$', views.cursoRedes, name='Redes'),
    url(r'^listaCurso/$', views.listaCurso, name='listaCurso'),
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    url(r'^esqueceuSenha/$', views.esqueceuSenha, name='esqueceuSenha'),
    url(r'^detalhesCurso/$', views.detalhesCurso, name='detalhesCurso'),
    url(r'^cursoProducao/$', views.cursoProducao, name='cursoProducao'),


    #url(r'^admin/', include(admin.site.urls)),
]