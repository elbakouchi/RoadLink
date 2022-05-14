from django.contrib import admin
from .models import Vehicle, Parking
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin
from provider.models import Insurance


class InsuranceInline(admin.TabularInline):
    extra = 1
    model = Insurance


class VehicleAdmin(ImportExportActionModelAdmin):
    inlines = [
        InsuranceInline,
    ]


admin.site.register(Parking)
admin.site.register(Vehicle, VehicleAdmin)


class VehicleResource(resources.ModelResource):
    class Meta:
        model = Vehicle
        fields = ('brand', 'model', 'registration_plate', 'parking__name', 'mileage',)
