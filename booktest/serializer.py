from rest_framework import serializers
from .models import BookInfo,HeroInfo

class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields="__all__"

class HeroInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeroInfo
        fields="__all__"