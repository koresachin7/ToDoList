from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)