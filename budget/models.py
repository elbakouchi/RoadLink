from django.db import models
from vehicle.models import Vehicle


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


