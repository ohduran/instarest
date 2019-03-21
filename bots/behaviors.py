from django.contrib.auth.hashers import make_password
from django.db import models


# Keep alphabetical order
class PasswordEncryptable(models.Model):
    password = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def clean(self):
        self.password = make_password(self.password)
        return super().clean()


class Verifiable(models.Model):
    is_verified = models.BooleanField(default=False)
    last_verified = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
