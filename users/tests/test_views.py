import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
class TestTokenCreateView:

    def test_post_should_login_user(self, tp):
        user_data = {
            'username': 'john',
            'password': 'secret',
            'email': 'john@beatles.com',
        }
        user = User.objects.create_user(**user_data)
        with pytest.raises(User.auth_token.RelatedObjectDoesNotExist):
            assert not user.auth_token
        data = {
            'username': user_data['username'],
            'password': user_data['password'],
        }
        response = tp.post('login', data=data)
        user.refresh_from_db()
        assert response.data['auth_token'] == user.auth_token.key


@pytest.mark.django_db
class TestUserViewSet:

    def test_authenticatedUser_shouldGetAListOfUsers(self, tp, default_user, client):

        headers = 'Token {}'.format(default_user.auth_token.key)
        response = client.get(reverse('users:user-list'), HTTP_AUTHORIZATION=headers)

        expected_response = [{
            'username': default_user.username,
            'email': default_user.email,
            'is_staff': False
        }]

        assert expected_response == response.json()

    def test_unauthenticatedUser_shouldGetAnError(self, tp):
        response = tp.get('users:user-list')

        assert {"detail": "Authentication credentials were not provided."} == response.json()
