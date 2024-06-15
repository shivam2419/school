from django.contrib import admin
from django.urls import path
from school_app import views

urlpatterns = [
    path("",views.index),
    path("index",views.index, name='index'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path("admission",views.admission, name='admission'),
    path("admission2",views.admission2, name='enquire'),
    path("reg_submit",views.register),
    path("events",views.EventInfo, name='EventInfo'),
    path("service",views.service, name='service'),
    path("Gallery",views.gallery),
    # admin section
    path("Dashboard",views.admin_dashboard, name='Dashboard'),
    path("enquiry_info/<str:pk>",views.EnquiryInfo, name='Enquiry'),
    path("activities",views.Activities_images, name='Activities'),
    path("events_data",views.Events, name='Events'),
    path("notices",views.Notices, name='Notice'),
    path("schoolgallery",views.deleteNotice, name='School_gallery'),
    # delete section
    path("Delete-Activities/<str:pk>",views.deleteActivity, name='deleteActivities'),
    path("deleteevent/<str:pk>",views.deleteEvent, name='deleteEvent'),
    path("deletenotice/<str:pk>",views.deleteNotice, name='deleteNotice'),
]
