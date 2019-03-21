from unittest.mock import patch

import pytest
from bots.models import Bot
from common.tests import TimestampableTests
from django.test.utils import override_settings
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status

from .. import messages


@pytest.mark.django_db
class TestBotViewSet(TimestampableTests):
    model = Bot

    def create_instance(self, **kwargs):
        return Bot.objects.create(**kwargs)

    def test_Post_GivenUsernameAndPassword_SlugIsUsername(self, default_user, client):
        data = {'username': 'test', 'password': 'testpassword'}
        headers = 'Token {}'.format(default_user.auth_token.key)
        response = client.post(reverse('bots:bot-list'), data=data, HTTP_AUTHORIZATION=headers)

        assert status.HTTP_201_CREATED == response.status_code
        expected_json = {'id': 1, 'username': 'test', 'is_verified': False}
        assert expected_json == response.json()

        assert 1 == Bot.objects.count()

        bot = Bot.objects.first()

        assert 'test' == bot.slug

    @override_settings(task_always_eager=True)
    def test_Verify_GivenCorrectUsernameAndPassword_isVerifiedTurnsTrue(self, default_user, client):
        headers = 'Token {}'.format(default_user.auth_token.key)

        bot = mommy.make(Bot, username='username', password='password', pk=1)
        assert bot.is_verified is False

        with patch('bots.views.tasks.get_session', return_value=True) as mock:
            response = client.get(reverse('bots:bot-verify', args=[1]), HTTP_AUTHORIZATION=headers)
        mock.assert_called_once()

        assert status.HTTP_200_OK == response.status_code
        assert {'detail': messages.VERIFYING_BOT} == response.json()

        bot.refresh_from_db()
        assert bot.is_verified
