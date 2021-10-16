from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=40)
    player = models.ManyToManyField(User)

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    