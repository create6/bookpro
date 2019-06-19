from rest_framework import serializers
from .models import BookInfo

class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInfo
        fields="__all__"