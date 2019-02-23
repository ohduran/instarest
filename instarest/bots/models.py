from django.db import models

from .behaviors import Permalinkable, Timestampable, Verifiable


class BotManager(models.Manager):
    use_for_related_fields = True

    def verified(self, **kwargs):
        return self.filter(is_verified=True, **kwargs)


class Bot(Timestampable, Verifiable, Permalinkable, models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    objects = BotManager()
