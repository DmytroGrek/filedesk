from django.conf.urls import url
from depos_app import views

# Why here home but in main urls.py it's 'distributives/'???
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^download/', views.download, name='download')
]
