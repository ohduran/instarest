import pytest
from accounts.models import Account
from bots.models import Bot
from common.tests import PermalinkableTests, TimestampableTests
from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from users.models import User
from users.tests import HasUserMixinTests

from .behavior_tests import IsVerifiableTests


@pytest.mark.django_db
class TestBotViewSet(TimestampableTests, PermalinkableTests, IsVerifiableTests, HasUserMixinTests):
    model = Bot

    def create_instance(self, **kwargs):
        return Bot.objects.create(**kwargs)

    def create_instance_with_user(self, **kwargs):
        user_data = {
            'username': 'john',
            'password': 'secret',
            'email': 'john@beatles.com',
        }
        user = User.objects.create_user(**user_data)
        return Bot.objects.create(user=user)

    def test_Post_GivenUsernameAndPassword_aBotInstanceIsCreated(self, default_user, client):
        data = {'username': 'test', 'password': 'testpassword'}
        headers = 'Token {}'.format(default_user.auth_token.key)
        response = client.post(reverse('bots:bot-list'), data=data, HTTP_AUTHORIZATION=headers)

        assert status.HTTP_201_CREATED == response.status_code
        expected_json = {'id': 1, 'username': 'test', 'is_verified': False}
        assert expected_json == response.json()

        assert 1 == Bot.objects.count()

        bot = Bot.objects.first()

        assert data['username'] == bot.username
        assert data['password'] == bot.password

    def test_Post_GivenABotAndAnAccount_BotWillFollowAccount(self, default_user, client):
        headers = 'Token {}'.format(default_user.auth_token.key)

        bot = self.create_instance()
        bot.assign_user(default_user.pk)
        account = mommy.make(Account, pk=1)

        data = {
            'ids': [1],
        }

        response = client.post(reverse('bots:bot-follow', args=[bot.pk]), data=data, HTTP_AUTHORIZATION=headers)
        assert status.HTTP_201_CREATED == response.status_code
