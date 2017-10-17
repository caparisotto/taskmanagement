# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciador', '0002_auto_20171003_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riscos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=300, null=True)),
                ('resolucao', models.CharField(max_length=300, null=True)),
                ('severidade', models.CharField(choices=[('Rara', 'Rara'), ('Baixa', 'Baixa'), ('M\xe9dia', 'M\xe9dia'), ('Alta', 'Alta'), ('Cr\xedtica', 'Cr\xedtica')], max_length=20)),
                ('probabilidade', models.CharField(choices=[('Rara', 'Rara'), ('Baixa', 'Baixa'), ('M\xe9dia', 'M\xe9dia'), ('Alta', 'Alta'), ('Cr\xedtica', 'Cr\xedtica')], max_length=20)),
            ],
        ),
    ]
