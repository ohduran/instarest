from django.db import models


# Keep alphabetical order
class Permalinkable(models.Model):
    slug = models.SlugField()

    class Meta:
        abstract = True

    def get_url_kwargs(self, **kwargs):
        kwargs.update(getattr(self, 'url_kwargs', {}))
        return kwargs

    def get_absolute_url(self):
        url_kwargs = self.get_url_kwargs(slug=self.slug)
        return (self.url_name, (), url_kwargs)

    def pre_save(self, instance, add):
        from django.utils.text import slugify
        if not instance.slug:
            instance.slug = slugify(self.slug_source)


class Timestampable(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Verifiable(models.Model):
    verified = models.BooleanField(default=False)

    class Meta:
        abstract = True


class VerifiableQuerySet(models.query.QuerySet):
    def is_verified(self):
        return self.filter(verified=True)
