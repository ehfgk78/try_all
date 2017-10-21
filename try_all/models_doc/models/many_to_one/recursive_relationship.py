from django.db import models
# Create your models here.

__all__ = (
    'User',
)

class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} - {self.teacher}'

    #save() override
    def save(self, *args, **kwargs):
        print('User save')
        if self.teacher and self.teacher.pk == self.pk:
            print('teacher cannot self')
            self.teacher = None
        super().save(*args, **kwargs)

