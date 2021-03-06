from django.db import models

__all__ = (
    'Manufacturer',
    'Car',
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'
