# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Projeto(models.Model):
     nome = models.CharField(max_length=50)
     descricao = models.CharField(max_length=300,null=True)
     #horasdia = models.IntegerField(null=True)
     pessoa = models.ManyToManyField('Pessoa')
     datainicio = models.DateTimeField(null=True)
     def __unicode__(self):
        return self.nome

class Pessoa(models.Model):
     nome = models.CharField(max_length=50)
     def __unicode__(self):
        return self.nome

class Status(models.Model):
     nome = models.CharField(max_length=50)
     ordem = models.IntegerField(default=0)
     def __unicode__(self):
        return self.nome


niveis = (
        ("Rara", "Rara"),
        ("Baixa", "Baixa"),
        ("Média", "Média"),
        ("Alta", "Alta"),
        ("Crítica", "Crítica"),
        )


class Riscos(models.Model):
     nome = models.CharField(max_length=50)
     projeto = models.ForeignKey(Projeto)
     descricao = models.CharField(max_length=300,null=True)
     resolucao = models.CharField(max_length=300,null=True)
     severidade = models.CharField(max_length=20,choices=niveis)
     probabilidade = models.CharField(max_length=20,choices=niveis)
     def __unicode__(self):
        return self.nome    

class Tarefa(models.Model):
     nome = models.CharField(max_length=50)
     pessoa = models.ForeignKey(Pessoa,null=True)
     projeto = models.ForeignKey(Projeto)
     status = models.ForeignKey(Status,null=True)
     progresso = models.IntegerField(default=0)
     duracao = models.IntegerField("Duracao(em dias)",null=True)
     antecessor = models.ManyToManyField('self',related_name="ant",symmetrical=False)
     subtarefade = models.ForeignKey('self',verbose_name="Subtarefa De",related_name="subtarefa",null=True)
     solucao = models.ForeignKey(Riscos,verbose_name="Solucao para",null=True)
     def __unicode__(self):
        return self.nome
