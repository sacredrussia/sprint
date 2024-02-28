from django.db import models

new = 'NW'
pending = 'PG'
accepted = 'AD'
rejected = 'RD'

STATUS = [
    (new, 'новая запись'),
    (pending, 'модератор взял в работу'),
    (accepted, 'модерация прошла успешно'),
    (rejected, 'модерация прошла, информация не принята'),
]


class Users(models.Model):
    email = models.CharField(max_length=10000) #unique=True)
    fam = models.CharField(max_length=10000)
    name = models.CharField(max_length=10000)
    otc = models.CharField(max_length=10000)
    phone = models.CharField(max_length=10000)


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Passes(models.Model):
    new = 'NW'
    pending = 'PG'
    accepted = 'AD'
    rejected = 'RD'

    beautyTitle = models.CharField(max_length=10000)
    title = models.CharField(max_length=10000)
    other_titles = models.CharField(max_length=10000)
    connect = models.CharField(max_length=10000)
    add_time = models.DateTimeField()
    coordinates = models.ForeignKey(Coordinates, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    level_winter = models.CharField(max_length=10000)
    level_summer = models.CharField(max_length=10000)
    level_autumn = models.CharField(max_length=10000)
    level_spring = models.CharField(max_length=10000)
    status = models.CharField(max_length=256, choices=STATUS,)


class Images(models.Model):
    name = models.CharField(max_length=10000)
    passes = models.ForeignKey(Passes, on_delete=models.CASCADE, null=True)
