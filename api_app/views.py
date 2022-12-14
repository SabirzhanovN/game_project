from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from listings.models import Game
from.serializers import GameSerializer


class GameListAPIView(APIView):
    def get(self, request):
        data = Game.objects.all()
        context = {
            'posts': GameSerializer(data, many=True).data
        }

        return Response(context)
