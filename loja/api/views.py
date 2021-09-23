from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from loja.api import serializers
from loja.models import Loja


class LojasView(ListAPIView):
    serializer_class = serializers.LojaSerializer
    queryset = Loja.objects.all()

class LojasDetailView(RetrieveAPIView):
    serializer_class = serializers.LojaSerializer
    queryset = Loja

class LojaCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.LojaSerializer
    queryset = Loja

class LojaUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.LojaSerializer
    queryset = Loja

class LojaDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.LojaSerializer
    queryset = Loja