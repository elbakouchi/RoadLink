from django.contrib import admin
from .models import ServiceProvider, InsuranceProvider, GasSupplier


admin.site.register(ServiceProvider)
admin.site.register(InsuranceProvider)
admin.site.register(GasSupplier)