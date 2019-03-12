from rest_framework import viewsets

from .models import Followed
from .serializers import FollowedSerializer


class FollowedViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing bots.
    """
    queryset = Followed.objects.all()
    serializer_class = FollowedSerializer
