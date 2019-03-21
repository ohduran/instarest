from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.text import slugify


class CanBeFollowed(models.Model):

    bots = models.ManyToManyField('bots.Bot', related_name='following')

    class Meta:
        abstract = True
