from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class CustomerDetails(forms.Form):
    first_name = forms.CharField(label="Firstname", max_length=50)
    last_name = forms.CharField(label="Lastname", max_length=50)
    registration = forms.CharField(label = "Registration Number", max_length=50)
    # location = forms.CharField(label = "Location", max_length=100, required=False)
    check = forms.BooleanField(required = False)
class MechanicDetails(forms.Form):
     businessName = forms.CharField(label="BusinessName", max_length=100)
     businessId = forms.CharField(label= "Business Id", max_length=100)
     contact = forms.IntegerField(label = "Phone Number")
