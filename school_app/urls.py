from django.contrib import admin
from django.urls import path
from school_app import views

urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("about",views.about, name='index'),
    path("contact",views.contact),
    path("admission",views.admission),
    path("admission2",views.admission2),
    path("reg_submit",views.register),
    path("service",views.service),
    path("Gallery",views.gallery),
    path("Dashboard",views.admin_dashboard, name='Dashboard'),
    path("enquiry_info/<str:pk>",views.EnquiryInfo, name='Enquiry'),
    path("activities",views.Activities_images, name='Activities'),
    path("events",views.Events, name='Events'),
]
