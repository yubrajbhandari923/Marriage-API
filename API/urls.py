from .views import GameViewset, AddPlayerToGameView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'game', GameViewset, basename='game')
urlpatterns = router.urls
urlpatterns += [
    path('game/<int:game_id>/add-player/', AddPlayerToGameView.as_view()),
]