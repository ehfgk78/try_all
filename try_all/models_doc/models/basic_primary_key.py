from django.db import models


class Fruit(models.Model):
    name = models.CharField(
        max_length=100,
        primary_key=True
    )

    def __str__(self):
        return self.name
