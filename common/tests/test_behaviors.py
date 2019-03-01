class BehaviorTestMixin:

    def get_model(self):
        return getattr(self, 'model')

    def create_instance(self, **kwargs):
        raise NotImplementedError('Implement method')


class TimestampableTests(BehaviorTestMixin):

    def test_timestampable_object(self):
        from django.utils import timezone
        obj = self.create_instance(created_date=timezone.now())

        assert obj
