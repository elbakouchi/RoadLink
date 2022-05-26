from django.contrib import admin
from .models import Provider, InsuranceProvider, GasSupplier


admin.site.register(Provider)
admin.site.register(InsuranceProvider)
admin.site.register(GasSupplier)