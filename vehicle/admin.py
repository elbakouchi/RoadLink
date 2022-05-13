from django.contrib import admin
from .models import Vehicle, Parking
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportActionModelAdmin


class VehicleAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(Parking)
admin.site.register(Vehicle, VehicleAdmin)


class VehicleResource(resources.ModelResource):
    class Meta:
        model = Vehicle
        fields = ('brand', 'model', 'registration_plate', 'parking__name', 'mileage', )
