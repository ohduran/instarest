import pytest
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


@pytest.fixture
def default_user():
    data = {
        'username': 'john',
        'password': 'secret',
        'email': 'john@beatles.com',
    }
    user = User.objects.create_user(**data)
    user.raw_password = data['password']
    Token.objects.create(user=user)
    return user
