from django.db import models
from django.utils.text import slugify


# Keep alphabetical order
class Permalinkable(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Verifiable(models.Model):
    is_verified = models.BooleanField(default=False)

    class Meta:
        abstract = True
