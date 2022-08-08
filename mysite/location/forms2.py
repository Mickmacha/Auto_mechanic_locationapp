from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ReviewRating, Customer



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerDetails(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "registration"]


# class CustomerDetails(forms.Form):
#     first_name = forms.CharField(label="Firstname", max_length=50)
#     last_name = forms.CharField(label="Lastname", max_length=50)
#     registration = forms.CharField(label="Registration Number", max_length=50)
#     # location = forms.CharField(label = "Location", max_length=100, required=False)
#     check = forms.BooleanField(required=False)


class MechanicDetails(forms.Form):
    businessName = forms.CharField(label="BusinessName", max_length=100)
    businessId = forms.CharField(label="Business Id", max_length=100)
    contact = forms.IntegerField(label="Phone Number")


class ServiceDetails(forms.Form):
    vehicle_brand = forms.CharField(label="What is your brand?", max_length=100)
    vehicle_model = forms.CharField(label="What is your vehicles model?", max_length=100)
    problem_description = forms.CharField(label="Describe your car issues", max_length=500)


class ReviewForms(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']


class MechanicUpdateStatusForm(forms.Form):
    stat=(('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'))
    status=forms.ChoiceField( choices=stat)
    cost = forms.IntegerField()
# class UpdateCostForm(forms.Form):
