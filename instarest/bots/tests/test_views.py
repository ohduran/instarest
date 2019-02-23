import pytest
from model_mommy import mommy
from rest_framework import status

from ..models import Bot


@pytest.mark.django_db
class TestBotViewSet:

    def test_Post_GivenUsernameAndPassword_Returns201(self, tp):
        data = {'username': 'test', 'password': 'testpassword'}
        response = tp.post('bot-list', data=data, extra={'format': 'json'})

        expected_json = {'id': 1, 'slug': 'test', 'username': 'test', 'is_verified': False}
        assert expected_json == response.json()
        assert status.HTTP_201_CREATED == response.status_code

    # def test_Retrieve_GivenASlug_ReturnsTheCorrespondingInstance(self, tp):
    #     bot = mommy.make(Bot, username='test', slug='test', password='testpassword')
    #     url = tp.reverse('bot-detail', args=['test'])
    #
    #     response = tp.get(url)
    #     assert status.HTTP_200_OK == response.status_code
    #     assert response.json()
