#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.db import connection


class Certificados(models.Model):
	nome = models.CharField(max_length=20,unique=True,verbose_name="Nome do Cliente")
	aplicacao = models.CharField(max_length=75)
	descricao = models.CharField(max_length=100,null=True,blank=True)
	validade = models.DateTimeField(verbose_name="Data de Validade (Formato Americano)")
	certificadora = models.ForeignKey('Entidades',on_delete=models.PROTECT)
	def __unicode__(self):
		return self.aplicacao

class Entidades(models.Model):
	nome = models.CharField(max_length=30,unique=True)
	def __unicode__(self):
		return self.nome

class Email_Alertas(models.Model):
	mailorigem = models.CharField(max_length=50,unique=True,verbose_name="E-mail Origem")
	senha = models.CharField(max_length=50)
	smtpserver = models.CharField(max_length=50,verbose_name="Servidor SMTP")
	smtpport = models.IntegerField(verbose_name="Porta SMTP")
	maildestino = models.CharField(max_length=50,verbose_name="E-mail Destino")
