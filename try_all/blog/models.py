from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL) # 장고걸스와 다름
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        "게시글을 발행상태로 "
        self.published_date = timezone.now()
        self.save()

    def hide(self):
        "게시글을 미발행상태로 "
        self.published_date = None
        self.save()



