from django.db import models

__all__ = (
    'FacebookUser',
    'InstagramUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name


class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.name
