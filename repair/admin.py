from django.contrib import admin
from .models import Intervention, Maintenance
from provider.models import Provider

admin.site.register(Intervention)
admin.site.register(Maintenance)

