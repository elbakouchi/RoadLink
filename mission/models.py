from django.db import models

from vehicle.models import Vehicle
from district.models import District
from budget.models import Budget


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
    fuel = models.CharField('Type carburant', max_length=2, choices=fuel_CHOICES, default='D')
    observation = models.TextField('Observation', default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mission"
        verbose_name_plural = "Missions"
        ordering = ("-createdAt",)

    def __str__(self):
        return "%s - %s" % (self.beneficiary, self.vehicle)
