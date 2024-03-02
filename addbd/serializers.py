from rest_framework import serializers

from .models import Passes, Users, Coordinates, Images


class PassesSerializer(serializers.Serializer):
    beauty_title = serializers.CharField(max_length=10000)
    title = serializers.CharField(max_length=10000)
    other_titles = serializers.CharField(max_length=10000)
    connect = serializers.CharField(max_length=10000, read_only=True)
    add_time = serializers.DateTimeField()
    coordinates_id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    level_winter = serializers.CharField(max_length=10000, read_only=True)
    level_summer = serializers.CharField(max_length=10000, read_only=True)
    level_autumn = serializers.CharField(max_length=10000, read_only=True)
    level_spring = serializers.CharField(max_length=10000, read_only=True)
    status = serializers.CharField(max_length=10000, read_only=True)



