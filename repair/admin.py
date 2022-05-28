from django.contrib import admin
from .models import Intervention, Maintenance
from provider.models import Provider


class InterventionAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(InterventionAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_by': request.user.pk
        }


class MaintenanceAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(MaintenanceAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_id': request.user.pk
        }


admin.site.register(Intervention, InterventionAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
