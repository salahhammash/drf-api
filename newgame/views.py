from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer 

# Create your views here.

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer    
    