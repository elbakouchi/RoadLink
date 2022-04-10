from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicle.models import Vehicle
from provider.models import Provider
from django.contrib.auth.models import User


class Intervention(models.Model):
    name = models.CharField("Intitulé", max_length=150, default="")
    cost = models.DecimalField("Coût", default=1000.0, decimal_places=2, max_digits=7)
    provider = models.ForeignKey(Provider, blank=True, verbose_name="Prestataire", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.provider}"


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name="Véhicule")
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    contractedBy = models.CharField(default="", blank=True, max_length=150, verbose_name="Contracté par")
    supervision = models.CharField(default="", blank=True, max_length=150, verbose_name="Supervisé par")
    status_CHOICES = (
        ('S', 'Accomplie'),
        ('NS', 'Non accomplie')
    )
    status = models.CharField(
        max_length=2,
        choices=status_CHOICES,
        default='NS',
    )
    createdBy = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, verbose_name="Créé par")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-createdAt",)

    def __str__(self):
        return f"Intervention {self.vehicle} {self.intervention}"


'''
class Repair(models.Model):
    registeredDate = models.DateTimeField(default=timezone.now)
    status_CHOICES = (
        ('S', 'solved'),
        ('NS', 'not solved')
    )
    status = models.CharField(
        max_length=2,
        choices=status_CHOICES,
        default='NS',
    )
    registeredUser = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    issue = models.CharField(max_length=1000)

    def __str__(self):
        return 'issue : ' + self.issue

'''
