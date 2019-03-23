from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import messages, tasks
from .models import Bot
from .serializers import BotSerializer


class BotViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing bots.
    """
    queryset = Bot.objects.all()
    serializer_class = BotSerializer

    @action(detail=True, methods=['get'])
    def verify(self, request, pk=None):
        bot = self.get_object()
        tasks.verify_bot.delay(bot.username)
        return Response({'detail': messages.VERIFYING_BOT})

    @action(detail=True, methods=['post'])
    def follow(self, request, pk):
        bot = self.get_object()
        return Response({'detail': messages.FOLLOWING_ACCOUNTS}, status=status.HTTP_201_CREATED)
