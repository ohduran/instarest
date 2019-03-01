from django.utils import timezone
from freezegun import freeze_time


class BehaviorTestMixin:

    def get_model(self):
        return getattr(self, 'model')

    def create_instance(self, **kwargs):
        raise NotImplementedError('Implement method')


class TimestampableTests(BehaviorTestMixin):

    def test_timestampable_object(self):

        now = timezone.now()
        with freeze_time(now):
            obj = self.create_instance()

        assert now == obj.created_date
