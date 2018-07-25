#-*- Coding: UTF-8 -*-
#coding: utf-8
from __future__ import unicode_literals
from PIL import Image
from django.db import models

# Create your models here.
class Courses(models.Model):
    #criar os atrubutos do curso 
    name = models.CharField('Nome', max_length=100) #recebe primeiro um verbose
    slug= models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Inicio', null=True, blank=True
    )
    # add imagem 
    image = models.ImageField(
        upload_to='courses/image', verbose_name='Imagem'
    )

    created_at = models.DateField(
        'Criado em', auto_now=True
    )
    update_at = models.DateField(
        'Atualizado em', auto_now=True
    )
