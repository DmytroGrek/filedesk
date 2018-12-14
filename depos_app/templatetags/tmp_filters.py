# coding: utf-8
import os

from django.utils.translation import ugettext_lazy as _
from django.template import Library


register = Library()


@register.filter
def get_html_for_file(filename, url):
    name, extension = os.path.splitext(filename)
    download_link = "<a href='/download/?file={0}' title='{0}'>{1}</a>".format(
            filename, _('Скачать файл')
        )

    if extension.lower() in ('.jpeg', '.jpg', '.png', '.gif'):
        return "<div><img src='{}' alt='{}' width=200px><br>{}</div>".format(
            url, filename, download_link
        )
    else:
        return download_link
