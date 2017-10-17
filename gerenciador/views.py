# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, render_to_response
from models import *
from forms import *
from django.http import HttpResponseRedirect
import os

# Create your views here.

#projetos
def lista_projetos(request):
	lista = Projeto.objects.all().order_by('nome')
        return render(request, 'lista_projetos.html', {'lista': lista})

def editaprojeto(request, id):
        projeto = get_object_or_404(Projeto, id=id)
        form = FormProjeto(request.POST or None, instance=projeto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
                form = FormProjeto(instance=projeto)
        return render(request, 'editadd.html', {'form': form})

def adicionaprojeto(request):
        if request.method ==  "POST":
                form = FormProjeto(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/')
        else:
                form = FormProjeto()
        return render(request, 'editadd.html', {'form': form})

#pesosas
def lista_pessoas(request):
	lista = Pessoa.objects.all().order_by('nome')
        return render(request, 'lista_pessoas.html', {'lista': lista})

def editapessoa(request, id):
        pessoa = get_object_or_404(Pessoa, id=id)
        form = FormPessoa(request.POST or None, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listpessoas/')
        else:
                form = FormPessoa(instance=pessoa)
        return render(request, 'editadd.html', {'form': form})

def adicionapessoa(request):
        if request.method ==  "POST":
                form = FormPessoa(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/listpessoas/')
        else:
                form = FormPessoa()
        return render(request, 'editadd.html', {'form': form})

#tarefas
def lista_tarefas(request,id):
	lista = Tarefa.objects.filter(projeto=id).order_by('-progresso')
        for elemento in lista:
            elemento.cs = 0
            elemento.es = 0
            subt = Tarefa.objects.filter(subtarefade=elemento)
            if subt:
                elemento.cs = 1
                somad = 0
                somap = 0
                count = 0
                pessoas = []
                for valor in subt:
                    somad = somad + valor.duracao
                    somap = somap + valor.progresso
                    count+=1
                mediap = somap / count
                
                elemento.duracao = somad
                elemento.progresso = mediap
                elemento.pessoa = None
            if elemento.subtarefade != None:
                elemento.es = 1
        return render(request, 'lista_tarefas.html', {'lista': lista, 'projeto': id})

def editatarefa(request, id):
        tarefa = get_object_or_404(Tarefa, id=id)
        codproj = tarefa.projeto.id
        projeto = get_object_or_404(Projeto, id=codproj)
        form = FormTarefa(projeto,request.POST or None, instance=tarefa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listtasks/%s'%(codproj))
        else:
                form = FormTarefa(projeto,instance=tarefa)
        return render(request, 'editadd.html', {'form': form})

def adicionatarefa(request,id):
        projeto = get_object_or_404(Projeto, id=id)
        if request.method ==  "POST":
                form = FormTarefa(projeto, request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/listtasks/%s'%(id))
        else:
                form = FormTarefa(projeto)
        return render(request, 'editadd.html', {'form': form})

#riscos
def lista_riscos(request,id):
	lista = Riscos.objects.filter(projeto=id).order_by('probabilidade')
        return render(request, 'lista_riscos.html', {'lista': lista, 'projeto': id})

def editarisco(request, id):
        risco = get_object_or_404(Riscos, id=id)
        codproj = risco.projeto.id
        form = FormRisco(request.POST or None, instance=risco)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/listrisks/%s'%(codproj))
        else:
                form = FormRisco(instance=risco)
        return render(request, 'editadd.html', {'form': form})

def adicionarisco(request,id):
        if request.method ==  "POST":
                form = FormRisco(request.POST, request.FILES)
                if form.is_valid():
                    risco = form.save(commit=False)
                    projeto = get_object_or_404(Projeto, id=id)
                    risco.projeto=projeto
                    risco.save()
                    return HttpResponseRedirect('/listrisks/%s'%(id))
        else:
                form = FormRisco()
        return render(request, 'editadd.html', {'form': form})

#status
def lista_status(request):
	lista = Status.objects.all().order_by('ordem')
        return render(request, 'lista_status.html', {'lista': lista})

def editastatus(request, id):
        status = get_object_or_404(Status, id=id)
        form = FormStatus(request.POST or None, instance=status)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/liststatus/')
        else:
                form = FormStatus(instance=status)
        return render(request, 'editadd.html', {'form': form})

def adicionastatus(request):
        if request.method ==  "POST":
                form = FormStatus(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('/liststatus/')
        else:
                form = FormStatus()
        return render(request, 'editadd.html', {'form': form})

def lista_kanban(request,id):
	lista = Tarefa.objects.filter(projeto=id).filter(subtarefade=None).filter(solucao=None).order_by('nome')
	status = Status.objects.all().order_by('ordem')
        for elemento in lista:
            subt = Tarefa.objects.filter(subtarefade=elemento)
            for valor in subt:
                elemento.nome = "%s - S:%s" %(elemento.nome,valor.nome)
        return render(request, 'lista_kanban.html', {'lista_tarefas': lista, 'lista_status': status})

def lista_plano_ws(request,id):
	lista = Tarefa.objects.filter(projeto=id).order_by('id')
        proj = Projeto.objects.filter(id=id)
        listapessoas = Pessoa.objects.filter(projeto=proj)
        gera_plano(lista,proj,listapessoas)
        return render(request, 'plan.html', {'lista': lista, 'proj': proj})

def lista_plano(request,id):
	lista = Tarefa.objects.filter(projeto=id).filter(solucao=None).order_by('id')
        proj = Projeto.objects.filter(id=id)
        listapessoas = Pessoa.objects.filter(projeto=proj)
        gera_plano(lista,proj,listapessoas)
        return render(request, 'plan.html', {'lista': lista, 'proj': proj})

def gera_plano(lista,proj,listapessoas):
        with open('templates/done.csv', 'wb+') as destination:
            destination.write('')

        with open('templates/tasks.csv', 'wb+') as destination:
            destination.write('id,group,task,skill,effort,depends\n')
            for tarefa in lista:
                antecessoras = ""
                for i in tarefa.antecessor.all():
                    antecessoras = antecessoras + ":" + str(i.id)
                destination.write('%d,,%s,%s,%d,%s\n' %(tarefa.id,tarefa.nome,tarefa.pessoa.nome,tarefa.duracao,str(antecessoras[1:])) )

        with open('templates/people.csv', 'wb+') as destination:
            ultimac = 0
            destination.write('name,skills,colour\n')
            for pessoa in listapessoas:
                ultimac, cordesenho = get_color(ultimac)
                destination.write('%s,,%s\n' %(pessoa.nome,cordesenho) )

        os.system("cd templates && pytaskplan -p")

        return


def get_color(last):
    cor = []
    cor.append('empty')
    cor.append('blue')
    cor.append('yellow')
    cor.append('red')
    cor.append('green')

    return last+1,cor[last+1]
