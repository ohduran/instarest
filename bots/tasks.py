# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .models import Bot
from .selenium import get_session


@shared_task()
def verify_bot(username):
    bot = Bot.objects.get(username=username)
    if get_session(bot):
        bot.is_verified = True
        bot.save()
