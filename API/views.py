from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .serializers import GameSerializers, PlayerSerializers
from .models import Game, Player
# Create your views here.


class GameViewset(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
    permission_classes = [IsAuthenticated]
    
class AddPlayerToGameView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def post(self, request, game_id):
        try: 
            print(request.data)
            player_id = request.data['player_id']
        except Exception:
            return Response("{'details': 'please specify player_id '}", status=status.HTTP_400_BAD_REQUEST)
        game_obj = get_object_or_404(Game, pk=game_id)
        user_obj = get_object_or_404(User, pk=player_id)
        player_obj = Player.objects.create(user=user_obj)
        player_obj.save()

        game_obj.player.add(player_obj)
        game_obj.save()
        
        serializer = GameSerializers(data=game_obj)
        return Response(serializer.initial_data, status=status.HTTP_200_OK)
