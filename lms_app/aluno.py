from django.db import models
from lms_app.professor import Professor

class Aluno(models.Model):
    def __str__(self):
        return self.nome + self.email
    def save(self):
    	if self.login == "":
    		raise Exception('')
    	if self.email == "":
    	    self.email = 'email nao fornecido'
    	if len(Aluno.objects.filter(login=self.login)!=0:
    		raise Exception("")
    	super(Aluno,self).save()
    if len(Professor.objects.filter(login=self.login))==if len(Aluno.objects.filter(login=self.login):
    		raise Exception("")
        
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)