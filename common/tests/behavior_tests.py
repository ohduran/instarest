from django.utils import timezone
from freezegun import freeze_time


class BehaviorTestCaseMixin:

    def get_model(self):
        return getattr(self, 'model')

    def create_instance(self, **kwargs):
        raise NotImplementedError('Implement method')


class TimestampableTests(BehaviorTestCaseMixin):

    def test_created_date(self):

        now = timezone.now()
        with freeze_time(now):
            obj = self.create_instance()

        assert now == obj.created_date

    def test_modified_date(self):

        obj = self.create_instance()

        now = timezone.now()
        with freeze_time(now):
            obj.save()

        assert now == obj.modified_date


class PermalinkableTests(BehaviorTestCaseMixin):

    def test_givenAnObjectWithUsername_theSlugIsTheSlugifiedUsername(self, default_user, client):
        obj = self.create_instance(username='test')
        assert 'test' == obj.slug
