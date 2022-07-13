from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
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


class Service(models.Model):
    vehicle_model = models.CharField(max_length=40, null=False)
    vehicle_brand = models.CharField(max_length=40, null=False)
    problem_description = models.CharField(max_length=500, null=False)
    date = models.DateField(auto_now=True)
    cost = models.PositiveIntegerField(null=True)

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)

    stat = (
        ('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'),
        ('Repairing Done', 'Repairing Done'),
        ('Released', 'Released'))
    status = models.CharField(max_length=50, choices=stat, default='Pending', null=True)

    def __str__(self):
        return self.problem_description


class ReviewRating(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    mechanic = models.ForeignKey('Mechanic', on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject