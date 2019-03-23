from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from .models import User


# Keep alphabetical order
class HasUserMixin(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

    def assign_user(self, pk):
        if not self.user:
            self.user = User.objects.get(pk=pk)
        else:
            raise ValidationError('User already assigned: {}'.format(self.user.pk))
