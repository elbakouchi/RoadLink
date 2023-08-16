from django.contrib import admin
from .models import Provider, ServiceProvider, InsuranceProvider, GasSupplier


class ProviderAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(ProviderAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_by': request.user.pk
        }


class ServiceProviderAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(ServiceProviderAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_by': request.user.pk
        }


class InsuranceProviderAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']
    def expiring_insurance_message(self, request):
        pass


    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(InsuranceProviderAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_by': request.user.pk
        }


class GasSupplierAdmin(admin.ModelAdmin):
    # search_fields = ['company_name', 'website']
    # list_display = ['company_name', 'website', 'created_by']
    # raw_id_fields = ['created_by']

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating a provider.
        """
        get_data = super(GasSupplierAdmin, self).get_changeform_initial_data(request)
        return get_data or {
            'createdBy_by': request.user.pk
        }


admin.site.register(Provider, ProviderAdmin)
admin.site.register(ServiceProvider, ServiceProviderAdmin)
admin.site.register(InsuranceProvider, InsuranceProviderAdmin)
admin.site.register(GasSupplier, GasSupplierAdmin)
