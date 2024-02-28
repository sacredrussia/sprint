from rest_framework import serializers

from .models import Passes


class PassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passes
        fields = ('beautyTitle', 'title', 'other_titles')
