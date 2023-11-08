from django.contrib import admin
from django.urls import path
from school_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index),
    path("index",views.index),
    path("about",views.about),
    path("contact",views.contact),
    path("admission",views.admission),
    path("admission2",views.admission2),
    path("reg_submit",views.register),
    path("service",views.service),
    path("Gallery",views.gallery),
]
