from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Acquittance


class AcquittanceAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(Acquittance, AcquittanceAdmin)
