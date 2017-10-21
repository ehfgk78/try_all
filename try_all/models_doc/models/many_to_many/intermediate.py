from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField(
        blank=True,
        null=True,
    )
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set',
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommender = models.ManyToManyField(
        Idol,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField(
        blank=True,
        null=True,
    )
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name}' \
               f'-{self.idol.name}' \
               f'({self.is_active})'


# shell_plus
# for i in ['임나영', '주결정', '김세정', '강미나', '김도연', '최유정', '유연정', '정채연', '김청하', '김소혜', '전소미']:
#     Idol(name=i).save()
# for g in ['프리스틴', '구구단', '위키미키', '우주소녀', '다이아']:
#     Group(name=g).save()
