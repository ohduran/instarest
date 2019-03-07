from django.db import models
from django.utils.text import slugify


# Keep alphabetical order
class Completable(models.Model):
    is_complete = models.BooleanField(default=False)
    last_complete = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Permalinkable(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
