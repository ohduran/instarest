from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import tasks
from .models import Bot
from .serializers import BotSerializer


class BotViewSet(viewsets.ModelViewSet):
    """
    Provides a list of all bots available
    """
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

    @action(detail=True, methods=['get'])
    def check_bot(self, request, pk=None):
        """
        Retrieve whether the bot can be used.
        """
        bot = get_object_or_404(Bot, pk=pk)
        tasks.check_bot(username=bot.username, password=bot.password)
        serializer = self.get_serializer(bot)
        return Response(serializer.data)
