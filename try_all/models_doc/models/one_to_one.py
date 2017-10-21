from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    address = models.CharField(max_length=80)

    class Meta:
        verbose_name = '장소'
        verbose_name_plural = f'{verbose_name} 목록'

    def __str__(self):
        return f'{self.name} the place'


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
        parent_link=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.place.name} the restaurant'


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} the waiter at {self.restaurant}'
