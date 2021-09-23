from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from rest_framework.generics import DestroyAPIView

from loja.api.views import LojasView, LojasDetailView, LojaCreateAPIView, LojaUpdateAPIView, LojaDeleteAPIView

app_name = 'loja'
urlpatterns = [
    url(r'^listar/$', LojasView.as_view()),
    url(r'^adicionar/$', login_required(LojaCreateAPIView.as_view())),
    url(r'^editar/(?P<pk>[-\w]+)/$', login_required(LojaUpdateAPIView.as_view())),
    url(r'^excluir/(?P<pk>[-\w]+)/$', login_required(LojaDeleteAPIView.as_view())),
    url(r'^(?P<pk>[-\w]+)/$', login_required(LojasDetailView.as_view())),
]