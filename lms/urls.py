from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from lms_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^listaCurso/$', views.listaCurso, name='listaCurso'),
    url(r'^detalhesCurso/$', views.detalhesCurso, name='detalhesCurso'),
    url(r'^noticias/$', views.noticias, name='noticias'),
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    url(r'^esqueceuSenha/$', views.esqueceuSenha, name='esqueceuSenha'),
    #url(r'^admin/', include(admin.site.urls)),
]   