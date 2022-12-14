from django.urls import path

from . import views

urlpatterns = [
    path('games_list/', views.GameListAPIView.as_view(), name='game_list')
]