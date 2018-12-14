import os

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings

from depos_app.models import Album

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {'albums': albums})


def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, request.GET.get('file'))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as _f:
            response = HttpResponse(_f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


