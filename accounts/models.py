from common.behaviors import Timestampable
from django.db import models


class AccountQueryset(models.QuerySet):
    pass


class AccountManager(models.Manager):
    queryset_class = AccountQueryset
    use_for_related_fields = True

    def get_queryset(self):
        return self.queryset_class(self.model)


class Account(Timestampable, models.Model):
    username = models.CharField(max_length=50, unique=True)

    objects = AccountManager()

    def __str__(self):
        return '@{}'.format(self.username)
