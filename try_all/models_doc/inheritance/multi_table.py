from django.db import models

class PlaceInheritance(models.Model):
    name = models.CharField(max_length=50, default='ABC')
    address = models.CharField(max_length=80)

    def __str__(self):
        return f'{self.name} Restaurant'

class Supplier(models.Model):
    # place_ptr = models.OneToOneField(Place)
    supply_places = models.ManyToManyField(
        PlaceInheritance,
        related_name='supply_place_set',
        related_query_name='supply_place',
    )