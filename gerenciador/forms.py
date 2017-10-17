from models import *
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from django.contrib.admin.widgets import FilteredSelectMultiple


class FormProjeto(forms.ModelForm):
        class Meta:
                model = Projeto
                fields = ['nome', 'pessoa', 'datainicio', 'descricao', ]
                widgets = {
                        'datainicio': DateWidget(attrs={'id':"datainicio"}, usel10n = True, bootstrap_version=3),
                }
                def __init__(self, *args, **kwargs):
                    super(FormProjeto, self).__init__(*args, **kwargs)
#                    self.fields['pessoa'] = forms.ModelMultipleChoiceField(queryset=Pessoa.objects.all().order_by('nome'), required=False, widget=FilteredSelectMultiple("Pessoas", is_stacked=False))

class FormStatus(forms.ModelForm):
        class Meta:
                model = Status
                fields = ['nome', 'ordem', ]

class FormPessoa(forms.ModelForm):
        class Meta:
                model = Pessoa
                fields = ['nome', ]

class FormRisco(forms.ModelForm):
        class Meta:
                model = Riscos
                fields = ['nome', 'descricao', 'resolucao', 'severidade', 'probabilidade', ]

class FormTarefa(forms.ModelForm):
        class Meta:
                model = Tarefa
                fields = ['nome', 'projeto', 'pessoa', 'status', 'progresso', 'duracao', 'antecessor', 'subtarefade', 'solucao', ]
                widgets = {'projeto': forms.HiddenInput()}
        def __init__(self, projeto, *args, **kwargs):
                super(FormTarefa, self).__init__(*args, **kwargs)
                self.fields['antecessor'] = forms.ModelMultipleChoiceField(queryset=Tarefa.objects.filter(projeto=projeto).filter(solucao=None).order_by('nome'), required=False, widget=FilteredSelectMultiple("Tarefa", is_stacked=False))
                self.fields['subtarefade'] = forms.ModelChoiceField(queryset=Tarefa.objects.filter(projeto=projeto).order_by('nome'), required=False)
                self.fields['pessoa'] = forms.ModelChoiceField(queryset=Pessoa.objects.filter(projeto=projeto).order_by('nome'))
                self.fields['solucao'] = forms.ModelChoiceField(queryset=Riscos.objects.filter(projeto=projeto).order_by('nome'), required=False)
                self.fields['projeto'].initial = projeto
