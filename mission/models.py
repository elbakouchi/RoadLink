from django.db import models

from vehicle.models import Vehicle


class Mission(models.Model):
    vehicle = models.ForeignKey(Vehicle, default=None, on_delete=models.CASCADE, verbose_name="Véhicule")
    beneficiary = models.CharField(verbose_name="Bénéficiaire", max_length=200)
    division = models.ForeignKey(Di, default=None, on_delete=models.CASCADE, verbose_name="Véhicule")
