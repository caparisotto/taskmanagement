"""mbmonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from certificados.views import *
from backups.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),

    #APP Certificados
    url(r'certificados/$', inicial),
    url(r'certificados/email', email),
    url(r'certificados/testmail', testmail),
    url(r'certificados/listentity/', listaentidades),
    url(r'certificados/addentity/', adicionaentidades),
    url(r'certificados/editentity/(?P<id>\d+)/$', editaentidades),
    url(r'certificados/delentity/(?P<id>\d+)/$', deletaentidades),
    url(r'certificados/listcert/', listacertificados),
    url(r'certificados/addcert/', adicionacertificados),
    url(r'certificados/editcert/(?P<id>\d+)/$', editacertificados),
    url(r'certificados/delcert/(?P<id>\d+)/$', deletacertificados),
    url(r'certificados/renewcert/(?P<id>\d+)/$', renovacertificados),

    #APP Backups
    url(r'backups/ListJobsBacula/$', ListJobsBacula, name="Listar jobs do Bacula"),
    url(r'backups/EscolheIntervalo/$', EscolheIntervalo, name="Escolher tarefa"),
    url(r'backups/ListJobs/$', ListJobs, name="Listar Tarefas Personalizadas"),
#    url(r'backups/EscolheServer/$', EscolheServer, name="Escolher Servidor"),
]
