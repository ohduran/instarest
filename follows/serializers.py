from rest_framework import serializers

from .models import Followed


class FollowedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followed
        fields = ('username',)
