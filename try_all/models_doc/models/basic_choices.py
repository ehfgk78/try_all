from django.db import models

__all__ = (
    'Person',
)


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=50)
    shirt_size = models.CharField(
        max_length=1, choices=SHIRT_SIZES
    )

    def __str__(self):
        return f'{self.name}-{self.shirt_size}'
