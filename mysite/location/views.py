from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group, User
from . import utilities
from .forms2 import CreateUserForm, CustomerDetails, MechanicDetails, ServiceDetails,ReviewForms, MechanicUpdateStatusForm
# from .forms import SignupForm, LoginForm, CustomerDetails, MechanicDetails
from .models import Customer, Mechanic, Service
from .decorators import *
from django.db.models import Q
from django.db.models import Sum

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
            'latitude': location['lat'],
            'longitude': location['lon']
        }
        return render(request, "location/home.html", context)
    return render(request, "location/home.html")


# redirect users to the mechanic profile
# @allowed_users(allowed_roles=['mechanic', 'customer'])
@csrf_exempt
def index(request, id=None):
    if request.method == "POST":
        id = request.POST.get("enquire")
        mechanicset = Mechanic.objects.all().filter(id=id)
        print(mechanicset)
        for i in mechanicset:
            print(i.businessName)
        print(bool(id))
    context = {}
    return render(request, "location/profile.html", context)


location = utilities.current_address_by_api()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def homepage(request):
    return render(request, "location/homepage.html")


@csrf_exempt
def mechsearch(request):
    msg = None

    customerset = Customer.objects.all()
    mechanicset = Mechanic.objects.all()
    try:
        location = utilities.current_address_by_api()
        customer_gps = (location["latitude"], location["longitude"])
        location["city"] = "Nairobi"
        for i in mechanicset:
            if i.city == location["city"]:
                mechanic_gps = (i.latitude, i.longitude)
                print(i.city)
                print(location["city"])
                dist_cust_mech = utilities.compare_distance(customer_gps, mechanic_gps)
                # context ={"resultset": [i.id, i.businessName, i.businessId, i.contact, i.city]}
                context = {}
                context.setdefault("resultset", [])
                result = [i.id, i.businessName, i.businessId, i.contact, i.city, dist_cust_mech]
                print(result)
                context["resultset"].append(result)
                # distance = {"distance" : dist_cust_mech}
                print(context["resultset"])
                return render(request, "location/results.html", context)
            else:
                msg = {"msg": "No one is available"}
                context = {}
    except ValueError as v:
        print(v)
    return render(request, "location/results.html", {"context": context, "msg": msg})


# checking assigned work for mechanic
# @allowed_users(allowed_roles=['mechanic'])
def mechanic_work_assigned(request):
    mechanic = Mechanic.objects.all().filter(id=request.user.id)
    works = Service.objects.all().filter(mechanic=request.user.id)
    return render(request, 'location/mechanic_service_view.html', {'works': works, 'mechanic': mechanic})


# change status and cost of the current service on user
# @allowed_users(allowed_roles=['mechanic'])
def mechanic_update_service_view(request):
    mechanic = Mechanic.objects.all().filter(id=request.user.id)
    updateStatus = MechanicUpdateStatusForm()
    if request.method == 'POST':
        updateStatus = MechanicUpdateStatusForm(request.POST)
        if updateStatus.is_valid():
            enquiry_x = Service.objects.all().filter(id=request.user.id)
            enquiry_x.status = updateStatus.cleaned_data['status']
            enquiry_x.cost = updateStatus.cleaned_data['cost']
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/mechanic_service_html')
    return render(request, 'location/mechanic_update_status.html', {'updateStatus': updateStatus, 'mechanic': mechanic})

def fill_review_view(request):
    service = Service.objects.all().filter(id=request.user.id)
    updateReview = ReviewForms()
    if request.method == 'POST':
        updateReview = ReviewForms(request.POST)
        if updateReview.is_valid():
            enquiry_x = Service.objects.all().filter(id=request.user.id)
            enquiry_x.status = updateReview.cleaned_data['status']
            enquiry_x.cost = updateReview.cleaned_data['cost']
            enquiry_x.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/mechanic_service_html')
    return render(request, 'location/mechanic_update_status.html', {'updateStatus': updateStatus, 'mechanic': mechanic})


# user viewing service status
# @allowed_users(allowed_roles=['customer'])
def user_service_view(request):
    customer = Customer.objects.all().filter(user_id=request.user.id)
    work_in_progress = Service.objects.all().filter(customer=request.user.id, status='Repairing').count()
    work_completed = Service.objects.all().filter(customer=request.user.id).filter(Q(status="Repairing Done") | Q(status="Released")).count()
    serviceset = Service.objects.all().filter(customer=request.user.id)
    new_request_made = Service.objects.all().filter(customer=request.user.id).filter(Q(status="Pending") | Q(status="Approved")).count()
    bill = Service.objects.all().filter(customer_id=request.user.id).filter(Q(status="Repairing Done") | Q(status="Released")).aggregate(Sum('cost'))
    print(bill)
    dict = {
        'work_in_progress': work_in_progress,
        'work_completed': work_completed,
        'new_request_made': new_request_made,
        'bill': bill['cost__sum'],
        'customer': customer,
    }
    return render(request, 'location/customer_dashboard.html', context=dict)



# def mech_service(request, id=None):
#     mechanicset = Mechanic.objects.all().filter(id=id)
#     serviceset = Service.objects.all().filter(mechanic=id)
#     services = serviceset
#     if request.Method == "POST":
#         form = ServiceDetails(request.Post)


# def landing(request):
#     return render(request, "location/landing.html")


def index2(request):
    if request.method == "POST":
        context = {
            'address': utilities.current_address_by_api()
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
        context = {'form': form}
        return render(request, 'location/register.html', context)


# @unauthenticated_user
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
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, username, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('homepage')
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
            t = Customer(first_name=fname, last_name=lname, registration=reg)
            t.save()
            user = t.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CustomerDetails()
    return render(request, "location/customer.html", {"form": form})


def mechanic_view(request):
    if request.method == "POST":
        form = MechanicDetails(request.POST)
        if form.is_valid():
            bname = form.cleaned_data.get('businessName')
            bid = form.cleaned_data.get('businessId')
            contact = form.cleaned_data.get("contact")
            location = utilities.current_address_by_api()

            t2 = Mechanic(businessId=bid, businessName=bname, contact=contact, city=location["city"],
                          latitude=location["latitude"], longitude=location["longitude"])
            t2.save()
            user=t2.save()
            group = Group.objects.get(name='mechanic')
            user.groups.add(group)
        return HttpResponseRedirect("/%i" % t2.id)
    else:
        form = MechanicDetails()
        return render(request, "location/mechanic.html", {"form": form})

    # def get_mechanic(request):
    # customerset = Customer.objects.all()
    # mechanicset = Mechanic.objects.all()
    # for i in customerset:
    #     print(i)
