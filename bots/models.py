from common.behaviors import Permalinkable, Timestampable
from django.db import models

from instarest.users.mixins import HasUserMixin

from .behaviors import PasswordEncryptable, Verifiable


class BotQueryset(models.QuerySet):
    pass


class BotManager(models.Manager):
    queryset_class = BotQueryset
    use_for_related_fields = True

    def get_queryset(self):
        return self.queryset_class(self.model)

    def verified(self, **kwargs):
        return self.filter(is_verified=True, **kwargs)


class Bot(Timestampable, Verifiable, PasswordEncryptable, Permalinkable, HasUserMixin, models.Model):
    username = models.CharField(max_length=50, unique=True)

    objects = BotManager()

    def __str__(self):
        return '@{}'.format(self.username)
