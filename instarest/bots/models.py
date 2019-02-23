from django.db import models

from .behaviors import Permalinkable, Timestampable, Verifiable, VerifiableQuerySet


class BotQuerySet(VerifiableQuerySet, models.QuerySet):
    pass


class Bot(Permalinkable, Timestampable, Verifiable, models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    objects = BotQuerySet.as_manager()
    url_name = "bot"
