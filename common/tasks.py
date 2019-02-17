# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .utils import get_session


@shared_task()
def check_bot(username, password):
    """Check whether the bot is usable or not"""
    bot = get_session(username, password)
    return True
