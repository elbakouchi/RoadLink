from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicle.models import Vehicle
from provider.models import ServiceProvider
from django.contrib.auth.models import User


class Intervention(models.Model):
    name = models.CharField("Intitulé", max_length=150, default="")

    class Meta:
        verbose_name = "Type intervention"
        verbose_name_plural = "Types interventions"

    def __str__(self):
        return f"{self.name} {self.provider}"


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name="Véhicule")
    intervention = models.ForeignKey(Intervention, on_delete=models.CASCADE)
    cost = models.DecimalField("Coût", default=1000.0, decimal_places=2, max_digits=7)
    provider = models.ForeignKey(ServiceProvider, blank=True, verbose_name="Prestataire", on_delete=models.CASCADE)

    status_CHOICES = (
        ('P', 'En cours'),
        ('D', 'Accomplie')

    )
    status = models.CharField(
        max_length=1,
        choices=status_CHOICES,
        default='P',
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
