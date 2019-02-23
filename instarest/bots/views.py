from rest_framework import viewsets

from .models import Bot
from .serializers import BotSerializer


class BotViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing bots.
    """
    queryset = Bot.objects.all()
    serializer_class = BotSerializer
