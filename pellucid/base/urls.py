from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('foundation/<str:pk>', views.foundation, name="foundation"),
    path('donate.html', views.donate, name="donate"),
]
