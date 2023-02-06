from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('auction/<prod_id>', views.auction, name = "auction"),
    path('sign-up/', views.registration, name = "registration"),
    path('sign-in/', views.signin, name = "login"),
    path('sign-out/', views.signout, name = "logout"),
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('profile/', views.profile, name = "profile"),
]
