# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0004_riscos_projeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='antecessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='antecessora', to='gerenciador.Tarefa'),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='duracao',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='progresso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='sucessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sucessora', to='gerenciador.Tarefa'),
        ),
    ]
