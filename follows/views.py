from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Follow
from .serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for the collection of follows.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        pass
