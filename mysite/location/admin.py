from django.contrib import admin
from .models import Customer, Mechanic, ReviewRating, Service
# Register your models here.
# admin.site.register(User)
admin.site.register(Mechanic)
admin.site.register(Customer)
admin.site.register(ReviewRating)
admin.site.register(Service)
