# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depos_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='upload',
            field=models.FileField(blank=True, default='', upload_to='depos_app/media', verbose_name='Файл'),
        ),
    ]
