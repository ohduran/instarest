from django.db import models

from .behaviors import PasswordEncryptable, Permalinkable, Timestampable, Verifiable


class BotQueryset(models.QuerySet):
    pass


class BotManager(models.Manager):
    queryset_class = BotQueryset
    use_for_related_fields = True

    def get_queryset(self):
        return self.queryset_class(self.model)

    def verified(self, **kwargs):
        return self.filter(is_verified=True, **kwargs)


class Bot(Timestampable, Verifiable, PasswordEncryptable, Permalinkable, models.Model):
    username = models.CharField(max_length=50, unique=True)

    objects = BotManager()

    def __str__(self):
        return '@{}'.format(self.username)
