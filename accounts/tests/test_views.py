import pytest
from accounts.models import Account
from common.tests import TimestampableTests


@pytest.mark.django_db
class TestBotViewSet(TimestampableTests):
    model = Account

    def create_instance(self, **kwargs):
        return Account.objects.create(**kwargs)
