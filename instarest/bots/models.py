from django.db import models

from .behaviors import Permalinkable, Timestampable, Verifiable


class Bot(Timestampable, Verifiable, Permalinkable, models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
