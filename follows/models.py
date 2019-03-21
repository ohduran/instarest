from django.db import models

from .behaviors import CanBeFollowed


class Followed(CanBeFollowed, models.Model):

    username = models.CharField(max_length=20)
