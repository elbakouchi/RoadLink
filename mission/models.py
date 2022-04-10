from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse_lazy
from vehicle.models import Vehicle
from district.models import District
from budget.models import Budget, Acquittance
from organism.models import Organism
from django.templatetags.static import static
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
#from weasyprint.text.fonts import FontConfiguration
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import time


class Mission(models.Model):
    fuel_CHOICES = (
        ('D', 'Diesel'),
        ('G', 'Essence'),
        ('E', 'Eléctrique'),
        ('H', 'Hybride')

    )
    voucher_number = models.CharField('N° Bon', default="", max_length=50)
    vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE, verbose_name='Véhicule')
    beneficiary = models.CharField(verbose_name='Bénéficiaire', max_length=200, default="")
    district = models.ForeignKey(District, default=None, null=True, on_delete=models.CASCADE, verbose_name='Division')
    description = models.TextField('Mission', default="", blank=True)
    appointment = models.DateField('Date de mission', default=None)
    destination = models.CharField("Destination", default="", max_length=200, blank=True)
    budget = models.ForeignKey(Budget, default=None, null=True, on_delete=models.CASCADE, verbose_name="Budget")
    quantity = models.IntegerField('Quantité', default=1, blank=True)
    acquittance = models.ForeignKey(Acquittance, default=None, null=True,
                                    on_delete=models.CASCADE, verbose_name="Décharge")
    fuel = models.CharField('Type carburant', max_length=2, choices=fuel_CHOICES, default='D')
    observation = models.TextField('Observation', default="", blank=True)
    organism = models.ForeignKey(Organism, default=None, null=True,
                                 on_delete=models.CASCADE, verbose_name="Service")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Missions"
        ordering = ("-createdAt",)

    def __str__(self):
        return "%s - %s" % (self.beneficiary, self.vehicle)

    @admin.action(description='')
    def print_mission_voucher_button(self):
        return format_html(
            '<a href="{}" target="_blank" class="link"><img src="{}" alt="Imprimer" style="width:16px;"></a>',
            reverse_lazy("admin:admin_print_mission_voucher", args=[self.pk]),
            static('printer.png')
        )

    @admin.action(description='')
    def download_mission_voucher_button(self):
        return format_html(
            '<a href="{}" target="new" class="link"><img src="{}" alt="Télécharger" style="width:16px;"></a>',
            reverse_lazy("admin:admin_download_mission_voucher", args=[self.pk]),
            static('printer.png')
        )

    def get_fuelname(self):
        for fuel in self.fuel_CHOICES:
            if self.fuel == fuel[0]:
                return fuel[1]

    @admin.action(description='Imprimer bon de mission pour une mission pré-séléctionnée')
    def print_mission_voucher(self, disposition="attachment"):
        filename = f"bon-de-mission-{self.voucher_number}-{time.time()}.pdf"
        params = {
                  'beneficiary': self.beneficiary,
                  'mission': self.description,
                  'ministry': self.organism.ministry,
                  'province': self.organism.province,
                  'department': self.organism.department,
                  'service': self.organism.service,
                  'division': self.district,
                  'mission_date': self.appointment,
                  'destination': self.destination,
                  'vehicle': self.vehicle,
                  'amount': self.acquittance.amount,
                  'filename': filename,
                  'fuel': self.get_fuelname(),
                  'serial_number': self.voucher_number
                }
        # html = HTML(string='<h1>The title</h1>')
        # font_config = FontConfiguration()
        css = CSS(string='''
            @font-face {
                font-family: "Segoe UI";
                src: url(https://cdn.jsdelivr.net/npm/segoe-fonts@1.0.1/fonts/normal/segoeui.woff);
            }
            body { font-family: "Segoe UI" }''') #, font_config=font_config)
        html_string = render_to_string('mission/bon-mission.html', params)

        html = HTML(string=html_string)

        html.write_pdf(target=f'/tmp/{filename}', stylesheets=[css, "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"]) #, font_config=font_config)

        fs = FileSystemStorage('/tmp')
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'{disposition}; filename="{filename}"'
            return response

        return response
