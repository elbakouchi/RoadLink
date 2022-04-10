from django.db import models
from vehicle.models import Vehicle


class Allocations(models.IntegerChoices):
    BASIC = 1000, 'basique: 1000 DH'
    EXTRA = 1500, 'extra: 1500 DH'


class Budget(models.Model):
    title = models.CharField("Titre", max_length=100)
    fiscal_year_start = models.DateField(verbose_name="Date début d'exercice")
    fiscal_year_end = models.DateField(verbose_name="Date fin d'exercice")
    amount = models.DecimalField(verbose_name="Montant initial", decimal_places=2, max_digits=12)
    balance = models.DecimalField(verbose_name="Balance", decimal_places=2, max_digits=12)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.title, self.fiscal_year_start)

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
        ordering = ("-createdAt",)


class Acquittance(models.Model):
    serial_number = models.IntegerField("Numéro de décharge", default=None)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, default=None)
    beneficiary = models.CharField(verbose_name='Bénéficiaire', max_length=200, default="")
    allocation = models.IntegerField("Affectation", default=Allocations.BASIC, \
                                     choices=Allocations.choices)
    assignedAt = models.DateField("Date d'attribution", default=None)
    log_number = models.IntegerField("Numéro de carnet de bord", default=None)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=None)
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
