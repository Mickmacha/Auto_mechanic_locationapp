from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import utilities
from .forms2 import CreateUserForm,  CustomerDetails, MechanicDetails
# from .forms import SignupForm, LoginForm, CustomerDetails, MechanicDetails
from .models import Customer, Mechanic
from .decorators import *
from django.views import generic


# Create your views here.
# def index(request):
#     return HttpResponse("<h1> New Day</h1>")
login_required(login_url="login")
def home(request):
    if request.method == "POST":
        address = request.POST.get('address')
        location = utilities.get_location_by_address(address)
        context = {
            'latitude':location['lat'],
            'longitude':location['lon']
        }
        return render(request, "location/home.html", context)
    return render(request, "location/home.html")
def index(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        context = {
            'address':utilities.address_by_location(latitude, longitude)
        }
        return render(request, "location/index.html",context)
    return render(request, "location/index.html")
location = utilities.current_address_by_api()
def homepage(request):
    return render(request, "location/homepage.html")

def mech_search(request):
    customerset = Customer.objects.all()
    mechanicset = Mechanic.objects.all()
    location = utilities.current_address_by_api()
    customer_gps = (location["latitude"], location["longitude"])
    for i in mechanicset:
        if i.city == location["city"]:
             mechanic_gps = (i.latitude, i.logitude)
             dist_cust_mech = utiilities.compare_distance(customer_gps, mechanic_gps)
             context = {i.id : [i.businessName, i.businessId, i.contact, i.city, dist_cust_mech]}
             return render(request, "location/results.html", context)
        return render(request, "location/results.html")

# class search_list(generic.ListView):
#      customerset = Customer.objects.all()
#      mechanicset = Mechanic.objects.all()

def landing(request):
    return render(request, "location/landing.html")

def index2(request):
    if request.method == "POST":

        context = {
            'address':utilities.current_address_by_api()
        }
        return render(request, "location/loc.html", context)
    return render(request, "location/loc.html")
# @unauthenticated_user
# def register(request):
#     msg=None
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             msg = "User Created"
#             return redirect("login_view")
#         else:
#             msg = "form isn't valid"
#     else:
#         form=SignupForm()
#     return render(request, "location/register.html", {"form":form, "msg":msg})
@unauthenticated_user
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login_view')
        context = {'form':form}
        return render(request, 'location/register.html', context)
#@unauthenticated_user
# def login_view(request):
#     form = LoginForm(request.POST or None)
#     msg=None
#     if request.method == "POST":
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 return redirect('home')
#             else:
#                 msg = "Invalid username or password"
#         else:
#             msg = "error while validating form data"
#     return render(request, "location/login.html", {"form":form, "msg":msg})
@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, username, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            messages.info(username, "error while validating form data")
            return render(request, 'location/login.html', context)
    context = {}
    return render(request, 'location/login.html', context)
def logoutuser(request):
    logout(request)
    return redirect('login_view')
def customer_view(request):
    if request.method == "POST":
        form = CustomerDetails(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            reg = form.cleaned_data.get('registration')
            # loc = form.cleaned_data.get('location')
            t = Customer(first_name=fname,last_name=lname,registration=reg)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CustomerDetails()
    return render(request, "location/customer.html", {"form":form})
def mechanic_view(request):
    if request.method == "POST":
        form = MechanicDetails(request.POST)
        if form.is_valid():
            bname = form.cleaned_data.get('businessName')
            bid = form.cleaned_data.get('businessId')
            contact = form.cleaned_data.get("contact")
            location = utilities.current_address_by_api()

            t2 = Mechanic(businessId=bid, businessName=bname, contact=contact, city=location["City"], latitude=location["latitude"], longitude=location["longitude"])
            t2.save()
        return HttpResponseRedirect("/%i" %t2.id)
    else:
        form  = MechanicDetails()
    return render(request, "location/mechanic.html", {"form":form})
    # def get_mechanic(request):
        # customerset = Customer.objects.all()
        # mechanicset = Mechanic.objects.all()
        # for i in customerset:
        #     print(i)
