from django.urls import path
from django.shortcuts import redirect, get_object_or_404
from django.contrib import admin, messages
from .models import Mission


class MissionAdmin(admin.ModelAdmin):
    list_display = ("voucher_number", "vehicle", "beneficiary",
                    "district", "download_mission_voucher_button",
                    "print_mission_voucher_button")
    actions = [Mission.print_mission_voucher]

    def save_model(self, request, obj, form, change):
        messages.add_message(request, messages.INFO, 'Merci de mettre à jour le kilométrage du véhicule')
        super(MissionAdmin, self).save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('print/<int:pk>/', self.print_mission_voucher, name="admin_print_mission_voucher"),
            path('download/<int:pk>/', self.download_mission_voucher, name="admin_download_mission_voucher"),
        ]
        return my_urls + urls

    def download_mission_voucher(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        return mission.print_mission_voucher('attachment')

    def print_mission_voucher(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        return mission.print_mission_voucher('inline')


admin.site.register(Mission, MissionAdmin)
