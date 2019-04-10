import pytest
from common.tests import BehaviorTestCaseMixin
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class UserBehaviorTestCaseMixin(BehaviorTestCaseMixin):

    def create_instance_with_user(self, **kwargs):
        raise NotImplementedError("Implement me")


class HasUserMixinTests(UserBehaviorTestCaseMixin):
    def test_has_user(self):
        obj = self.create_instance_with_user()
        assert obj.user

    def test_assign_user(self):
        obj = self.create_instance()
        user_data = {
            'username': 'john',
            'password': 'secret',
            'email': 'john@beatles.com',
        }
        user = User.objects.create_user(**user_data)

        obj.assign_user(user.pk)

        assert obj.user == user

    def test_assign_user_fails_if_user_is_already_assigned(self):
        obj = self.create_instance_with_user()
        with pytest.raises(ValidationError):
            obj.assign_user(obj.user.pk)
