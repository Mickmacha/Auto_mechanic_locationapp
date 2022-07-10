from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path('',views.landing, name="landing"),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logoutuser, name="logout"),
    path('register', views.register, name="register"),
    path('home',views.home, name="home"),
    path('homepage', views.homepage, name="homepage"),
    path('customer',views.customer_view, name = 'customer_view'),
    path('mechanic', views.mechanic_view, name='mechanic_view'),
    path('index',views.index,name="index"),
    path('index2', views.index2, name="index2"),


]
#add login url
# path("<int:id>", views.index, name="index"),
