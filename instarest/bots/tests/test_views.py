import pytest
from rest_framework import status

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
