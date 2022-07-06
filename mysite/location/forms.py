# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# # from .models import User
#
# class LoginForm(forms.Form):
#     username = forms.CharField(
#                 widget=forms.TextInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
#     password = forms.CharField(
#                 widget=forms.PasswordInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
# roles = [('Mecahnic','Mecahnic'), ('Customer', 'Customer')]
# class SignupForm(forms.Form, forms.ModelForm):
#     username = forms.CharField(
#                 widget=forms.TextInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
#     password = forms.CharField(
#                 widget=forms.PasswordInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
#     password1 = forms.CharField(
#                 widget=forms.PasswordInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
#     email = forms.CharField(
#                 widget=forms.TextInput(
#                 attrs={
#                 "class": "form-control"
#                 }
#             )
#         )
#     role = forms.CharField(label="Role",
#                 widget=forms.RadioSelect(choices=roles)
#                 )
#     class Meta:
#         model = User
#         fields = ("username", "email", "password","password1","role")
# class CustomerDetails(forms.Form):
#     first_name = forms.CharField(label="Firstname", max_length=50)
#     last_name = forms.CharField(label="Lastname", max_length=50)
#     registration = forms.CharField(label = "Registration Number", max_length=50)
#     # location = forms.CharField(label = "Location", max_length=100, required=False)
#     check = forms.BooleanField(required = False)
# class MechanicDetails(forms.Form):
#      businessName = forms.CharField(label="BusinessName", max_length=100)
#      businessId = forms.CharField(label= "Business Id", max_length=100)
#      contact = forms.IntegerField(label = "Phone Number")
