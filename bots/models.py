from django.db import models

from .behaviors import Permalinkable, Timestampable, Verifiable


class BotQueryset(models.QuerySet):
    pass


class BotManager(models.Manager):
    queryset_class = BotQueryset
    use_for_related_fields = True

    def get_queryset(self):
        return self.queryset_class(self.model)

    def verified(self, **kwargs):
        return self.filter(is_verified=True, **kwargs)


class Bot(Timestampable, Verifiable, Permalinkable, models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    objects = BotManager()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return '@{}'.format(self.username)
