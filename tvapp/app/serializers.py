from rest_framework import serializers
from .models import TVShow

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'name', 'rating', 'network')
class ShowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('id', 'name', 'description', 'network', 'episodes', 'cast', 'rating')
# class ShowCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TVShow
#         fields = ('name', 'description', 'network', 'episodes', 'cast', 'rating')
# class ShowUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TVShow
#         fields = ('name', 'description', 'network', 'episodes', 'cast', 'rating')
class ShowOtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ('name', 'description', 'network', 'episodes', 'cast', 'rating')
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'network': {'required': False},
            'episodes': {'required': False},
            'cast': {'required': False},
            'rating': {'required': False},
        }