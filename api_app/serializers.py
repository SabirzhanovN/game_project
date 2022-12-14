from rest_framework import serializers
from listings.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('category', 'author', 'title',
                  'description', 'country', 'price',
                  'price_free', 'RAM', 'support_on_windows',
                  'support_on_mac', 'support_on_linux', 'is_published',
                  'list_date', 'photo_main', 'photo_1',
                  'photo_2', 'photo_3', 'photo_4',
                  'photo_5', 'photo_6')