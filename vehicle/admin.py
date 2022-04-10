from django.contrib import admin
from .models import Vehicle, Parking
from import_export.admin import ImportExportActionModelAdmin


class VehicleAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(Parking)
admin.site.register(Vehicle, VehicleAdmin)
