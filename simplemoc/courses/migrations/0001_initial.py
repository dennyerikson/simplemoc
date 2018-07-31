# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-31 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descri\xe7\xe3o')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de Inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/image', verbose_name='Imagem')),
                ('created_at', models.DateField(auto_now=True, verbose_name='Criado em')),
                ('update_at', models.DateField(auto_now=True, verbose_name='Atualizado em')),
            ],
        ),
    ]
