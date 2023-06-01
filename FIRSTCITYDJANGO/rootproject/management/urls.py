from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('management', views.Patient_list),
]