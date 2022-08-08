from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logoutuser, name="logout"),
    path('register', views.register, name="register"),
    path('home', views.home, name="home"),
    path('homepage', views.homepage, name="homepage"),
    path('customer', views.customer_view, name='customer_view'),
    path('mechanic', views.mechanic_view, name='mechanic_view'),
    path('service_details', views.service_details, name="service_details"),
    path('mechsearch', views.mechsearch, name='mechsearch'),
    path('mechanic_work_assigned', views.mechanic_work_assigned, name='mechanic_work_assigned'),
    path('mechanic-update-service', views.mechanic_update_service_view,name='mechanic-update-service'),
    path('user_service_view', views.user_service_view, name='user_service_view'),
    path('ratings', views.fill_review_view, name='fill_review_view'),

    path('index', views.index, name="index"),
    path('index2', views.index2, name="index2"),


]
# add login url
# path("<int:id>", views.index, name="index"),
