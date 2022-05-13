from django.db import models
from budget.models import Budget
from vehicle.models import Vehicle
from organism.models import Affectation


class Allocations(models.IntegerChoices):
    BASIC = 1000, 'basique: 1000 DH'
    EXTRA = 1500, 'extra: 1500 DH'


class Acquittance(models.Model):
    serial_number = models.PositiveIntegerField("Numéro de décharge", default=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=None)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=None)
    beneficiary = models.CharField(verbose_name='Bénéficiaire', max_length=200, default="")
    affectedTo = models.ForeignKey(Affectation, on_delete=models.CASCADE, default=None, verbose_name="Affectation")
    assignedAt = models.DateField("Date d'attribution", default=None)
    log_number = models.IntegerField("Numéro de carnet de bord", default=None)
    amount = models.DecimalField("Montant", default=1000.0, decimal_places=2, max_digits=7)
    observation = models.TextField('Observation', default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.serial_number, self.beneficiary)

    class Meta:
        verbose_name = "Décharge"
        verbose_name_plural = "Décharges"
        ordering = ("-createdAt",)