from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#Create your models here.
# class User(AbstractUser):
#     is_admin = models.BooleanField('Is admin', default=False)
#     is_customer = models.BooleanField('Is customer', default=False)
#     is_mechanic = models.BooleanField('Is mechanic', default=False)
class Mechanic(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
      businessName = models.CharField(max_length=100)
      businessId = models.CharField(max_length=100)
      # location = models.CharField(max_length=100)
      contact = models.IntegerField(null=False)
      city = models.CharField(max_length=100, null=True)
      latitude = models.FloatField(null=True)
      longitude = models.FloatField(null=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    registration = models.CharField(max_length=200)
    # location = models.CharField(max_length=100, null=True)
