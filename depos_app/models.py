# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Album(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Имя файла'))
    description = models.TextField(verbose_name=_('Описание Дистрибутива'))
    upload = models.FileField(
        _('Файл'), upload_to='depos_app', max_length=100, blank=True
    )

    def __str__(self):
        return '{}'.format(self.title)
