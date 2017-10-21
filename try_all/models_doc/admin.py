from django.contrib import admin

# Register your models here.
from models_doc import models
from .inheritance import (
    School, Student, Teacher,
    Supplier, PlaceInheritance,
    Champion, Supporter, )
from .models import (
    Person, Fruit,
    Car, Manufacturer, User,
    Pizza, Topping, TwitterUser,
    FacebookUser, InstagramUser,
    Idol, Group, Membership,
    Place, Restaurant, Waiter,
)


class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank',)
    list_editable = ('rank',)
    ordering = ('rank',)


admin.site.register(Person)
admin.site.register(Fruit)
admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(User)

admin.site.register(Pizza)
admin.site.register(Topping)

admin.site.register(TwitterUser)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)

admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)

admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)

admin.site.register(PlaceInheritance)
admin.site.register(Supplier)

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)

admin.site.register(Champion, ChampionAdmin)
admin.site.register(Supporter, ChampionAdmin)
