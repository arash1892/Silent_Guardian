from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class User_Banners_Visited(models.Model):
    user_id_session = models.CharField(max_length=255)
    banners_visited = ArrayField(models.IntegerField(), size=10)
    campaign_visited = models.IntegerField(models.IntegerField)
    time_visited = models.DateTimeField()


class User_Banner_Clicked(models.Model):
    user_id_session = models.CharField(max_length=255)
    banner_clicked = models.IntegerField()