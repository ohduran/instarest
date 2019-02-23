from rest_framework import serializers

from .models import Bot


class BotSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, write_only=True)
    is_verified = serializers.BooleanField(read_only=True)

    class Meta:
        model = Bot
        fields = ('id', 'is_verified', 'username', 'password')
