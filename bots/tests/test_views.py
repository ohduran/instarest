from unittest.mock import patch

from django.test.utils import override_settings

import pytest
from model_mommy import mommy
from rest_framework import status

from .. import messages
from ..models import Bot


@pytest.mark.django_db
class TestBotViewSet:

    def test_Post_GivenUsernameAndPassword_SlugIsUsername(self, tp):
        data = {'username': 'test', 'password': 'testpassword'}
        response = tp.post('bot-list', data=data, extra={'format': 'json'})

        expected_json = {'id': 1, 'username': 'test', 'is_verified': False}
        assert expected_json == response.json()
        assert status.HTTP_201_CREATED == response.status_code

        assert 1 == Bot.objects.count()

        bot = Bot.objects.first()

        assert 'test' == bot.slug

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_Verify_GivenCorrectUsernameAndPassword_isVerifiedTurnsTrue(self, tp):

        bot = mommy.make(Bot, username='username', password='password', pk=1)
        assert bot.is_verified is False
        with patch('bots.views.tasks.get_session', return_value=True) as mock:
            url = tp.reverse('bot-verify', pk=1)
            response = tp.get(url)
        mock.assert_called_once()

        assert status.HTTP_200_OK == response.status_code
        assert {'detail': messages.VERIFYING_BOT} == response.json()

        bot.refresh_from_db()
        assert bot.is_verified
