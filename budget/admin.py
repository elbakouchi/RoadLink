from django.contrib import admin
from budget.models import Budget, Acquittance
from import_export.admin import ImportExportActionModelAdmin


class AcquittanceAdmin(ImportExportActionModelAdmin):
    pass


admin.site.register(Budget)
admin.site.register(Acquittance, AcquittanceAdmin)
