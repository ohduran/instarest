from unittest.mock import patch

from common.tests import BehaviorTestCaseMixin
from django.test.utils import override_settings
from django.urls import reverse
from rest_framework import status


class IsVerifiableTests(BehaviorTestCaseMixin):

    @override_settings(task_always_eager=True)
    def test_Verify_GivenCorrectUsernameAndPassword_isVerifiedTurnsTrue(self, default_user, client):
        headers = 'Token {}'.format(default_user.auth_token.key)

        obj = self.create_instance(pk=1)
        assert obj.is_verified is False

        with patch('{}.views.tasks.get_session'.format(self.model._meta.app_label), return_value=True) as mock:
            url = reverse('{}:{}-verify'.format(self.model._meta.app_label, self.model._meta.verbose_name), args=[1])
            response = client.get(url, HTTP_AUTHORIZATION=headers)
        mock.assert_called_once()

        assert status.HTTP_200_OK == response.status_code

        obj.refresh_from_db()
        assert obj.is_verified is True
