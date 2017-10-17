#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Create your views here.
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from models import *
from forms import *
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta

import smtplib
import sys
import commands
from email.MIMEText import MIMEText

def inicial(request):
        return render(request, 'certificados/inicial.html', )

def email(request):
        objeto = get_object_or_404(Email_Alertas, id=1)
        form = FormMail(request.POST or None, instance=objeto)
        if form.is_valid():
        	form.save()
                #return HttpResponseRedirect('/email/')
		mensagem = "Dados salvos com sucesso!"
        	return render(request, 'certificados/editmailmsg.html', {'form': form, 'mensagem': mensagem})
	
        else:
                form = FormMail(instance=objeto)

        return render(request, 'certificados/editmail.html', {'form': form})

def testmail(request):
        objeto = get_object_or_404(Email_Alertas, id=1)
	retmail,statusmail = enviamail(objeto.mailorigem,objeto.senha,objeto.maildestino,objeto.smtpserver,objeto.smtpport,1,None,None,None)
	if retmail == 0:
		mensagem = "Mensagem enviada!"
	else:
		mensagem = "Erro no envio - %s" %(statusmail)
        return render(request, 'certificados/editmailmsg.html', {'mensagem': mensagem})

def enviamail(origem,senha,destino,servidor,porta,tipo,cliente,aplicacao,data):
	try :
		serv=smtplib.SMTP()
   		serv.connect(servidor,porta)
   		serv.starttls()
   		serv.login(origem,senha)
                dataatual = formatdate(localtime = True)
		if tipo == 1:
			texto = "Essa é uma mensagem de testes vinda do futuro...não, brincadeira....vinda da aplicação de certificados."
   			msg1 = MIMEText("%s"% texto)
   			msg1['Subject']='Just Testing'
		else:
			texto = "Certificado do cliente %s para a aplicacao %s expira em %s" %(cliente,aplicacao,str(data))
   			msg1 = MIMEText("%s"% texto)
   			msg1['Subject']='Certificado Expirando'
   		msg1['From']=origem
   		msg1['To']=destino
                msg1['Date']=dataatual
   		serv.sendmail(origem,destino, msg1.as_string())
   		serv.quit()
	except Exception, e:
   		return 1,e
	else:
   		return 0,None



def listaentidades(request):
	lista = Entidades.objects.all().order_by('nome')
	print "okokokokokokokokoko"
        return render(request, 'certificados/listaec.html', {'lista': lista})

def adicionaentidades(request):
	if request.method ==  "POST":
		form = FormEntidade(request.POST, request.FILES)
		if form.is_valid():
			form.save()
        		return HttpResponseRedirect('/certificados/listentity/')
	else:
		form = FormEntidade()
        return render(request, 'certificados/editadd.html', {'form': form})

def editaentidades(request, id): 
    	objeto = get_object_or_404(Entidades, id=id)
	form = FormEntidade(request.POST or None, instance=objeto)
	if form.is_valid():
		form.save()
        	return HttpResponseRedirect('/certificados/listentity/')
	else:
		form = FormEntidade(instance=objeto)
	
        return render(request, 'certificados/editadd.html', {'form': form})

def deletaentidades(request, id):
    	objeto = get_object_or_404(Entidades, id=id)
	objeto.delete()
        return HttpResponseRedirect('/certificados/listentity/')


def listacertificados(request):
	lista = Certificados.objects.all().order_by('nome')
        return render(request, 'certificados/listac.html', {'lista': lista})

def adicionacertificados(request):
	if request.method ==  "POST":
		form = FormCertificado(request.POST, request.FILES)
		if form.is_valid():
			form.save()
        		return HttpResponseRedirect('/certificados/listcert/')
	else:
		form = FormCertificado()
        return render(request, 'certificados/editadd.html', {'form': form})

def editacertificados(request, id): 
    	objeto = get_object_or_404(Certificados, id=id)
	form = FormCertificadoNorenov(request.POST or None, instance=objeto)
	if form.is_valid():
		form.save()
        	return HttpResponseRedirect('/certificados/listcert/')
	else:
		form = FormCertificadoNorenov(instance=objeto)
	
        return render(request, 'certificados/editadd.html', {'form': form})

def deletacertificados(request, id):
    	objeto = get_object_or_404(Certificados, id=id)
	objeto.delete()
        return HttpResponseRedirect('/certificados/listcert/')

def renovacertificados(request, id):
    	objeto = get_object_or_404(Certificados, id=id)
	form = FormDate()
	if request.method == "POST":
		if 'dataform' in request.POST:
			form = FormDate(request.POST, request.FILES)
			if form.is_valid():
				date = form.cleaned_data['date']
				objeto.validade = date
		elif 'dataatual' in request.POST:
			objeto.validade = datetime.now() + timedelta(days=90)
		objeto.save()
        	return HttpResponseRedirect('/certificados/listcert/')
        return render(request, 'certificados/renova.html', {'form': form})
