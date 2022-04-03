from django.contrib import admin

# Register your models here.
from .models import Vehicle, Parking

# Register your models here.
admin.site.register(Parking)
admin.site.register(Vehicle)
