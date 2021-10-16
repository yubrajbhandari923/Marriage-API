from rest_framework import serializers
from .models import Game, Player
from django.contrib.auth.models import User
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','name', "player"]
        depth = 2

class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'full_name', 'username']
