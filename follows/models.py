from common.behaviors import Completable, Permalinkable, Timestampable
from django.db import models


class FollowQueryset(models.QuerySet):
    pass


class FollowManager(models.Manager):
    queryset_class = FollowQueryset
    use_for_related_fields = True

    def completed(self, **kwargs):
        return self.filter(is_complete=True, **kwargs)


class Follow(Completable, Timestampable, Permalinkable, models.Model):
    username = models.CharField(max_length=50, unique=True)
    bot = models.ForeignKey('bots.Bot', on_delete=models.CASCADE)

    objects = FollowManager()

    def __str__(self):
        return '@{}'.format(self.username)
