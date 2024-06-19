from django.contrib import admin
from .models import contact,event,activity,notice,registration,inaugration,assembly,function,Pt

# Register your models here.
admin.site.register(contact)
admin.site.register(event)
admin.site.register(activity)
admin.site.register(notice)
admin.site.register(registration)
admin.site.register(inaugration)
admin.site.register(assembly)
admin.site.register(function)
admin.site.register(Pt)
