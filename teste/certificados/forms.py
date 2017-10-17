#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from models import *

class FormMail(forms.ModelForm):
        class Meta:
                model = Email_Alertas
                fields = ['mailorigem', 'senha', 'smtpserver', 'smtpport', 'maildestino', ]
        senha = forms.CharField(max_length=50,widget=forms.PasswordInput(render_value = True),label="Senha")

class FormEntidade(forms.ModelForm):
        class Meta:
                model = Entidades
                fields = ['nome', ]

class FormCertificado(forms.ModelForm):
        class Meta:
                model = Certificados
                fields = ['nome', 'aplicacao', 'descricao', 'validade', 'certificadora', ]

class FormCertificadoNorenov(forms.ModelForm):
        class Meta:
                model = Certificados
                fields = ['nome', 'aplicacao', 'descricao', 'certificadora', ]

class FormDate(forms.Form):
	date = forms.DateField(label="Data de Validade (Formato Americano)",required=False)
