"""ProjectManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gerenciador.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', lista_projetos),
    url(r'editaprojeto/(?P<id>\d+)/$', editaprojeto),
    url(r'adicionaprojeto/', adicionaprojeto),

    url(r'listpessoas/', lista_pessoas),
    url(r'editapessoa/(?P<id>\d+)/$', editapessoa),
    url(r'adicionapessoa/', adicionapessoa),

    url(r'liststatus/', lista_status),
    url(r'editastatus/(?P<id>\d+)/$', editastatus),
    url(r'adicionastatus/', adicionastatus),

    url(r'listtasks/(?P<id>\d+)/$', lista_tarefas),
    url(r'editatasks/(?P<id>\d+)/$', editatarefa),
    url(r'adicionatasks/(?P<id>\d+)/$', adicionatarefa),

    url(r'listrisks/(?P<id>\d+)/$', lista_riscos),
    url(r'editarisks/(?P<id>\d+)/$', editarisco),
    url(r'adicionarisks/(?P<id>\d+)/$', adicionarisco),

    url(r'listkanban/(?P<id>\d+)/$', lista_kanban),
    url(r'listkanbanws/(?P<id>\d+)/$', lista_kanban_ws),
    url(r'listplan/(?P<id>\d+)/$', lista_plano),
    url(r'listplanws/(?P<id>\d+)/$', lista_plano_ws),
    url(r'listgantt/(?P<id>\d+)/$', lista_gantt),
    url(r'listganttws/(?P<id>\d+)/$', lista_gantt_ws),
]


