from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.email),
    url(r'^massmail/$', views.mail),
    url(r'^mail/$', TemplateView.as_view(template_name='mail.html'), name='mail'),
    url(r'^email/$', TemplateView.as_view(template_name='email.html'), name='email'),
    url(r'^accounts/', views.index, name='index')
]
