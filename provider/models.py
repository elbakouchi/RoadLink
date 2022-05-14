from django.db import models
from vehicle.models import Vehicle


class InsuranceProvider(models.Model):
    name = models.CharField("Intitulé", max_length=50, default="")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Assureur"
        verbose_name_plural = "Assureurs"
        ordering = ("-createdAt",)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    provider = models.ForeignKey(InsuranceProvider, verbose_name="Assureur", on_delete=models.CASCADE, blank=False,
                                 default=None)
    vehicle = models.ForeignKey(Vehicle, verbose_name="Véhicule", on_delete=models.CASCADE, blank=False, default=None)
    startDate = models.DateField(verbose_name="Date début", blank=True, null=False)
    endDate = models.DateField(verbose_name="Date expiration", blank=True, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Assurance"
        verbose_name_plural = "Assurances"
        ordering = ("-createdAt",)

    def __str__(self):
        return f"{self.provider.name}-{self.vehicle.model}-{self.vehicle.registration_plate}"


class Provider(models.Model):
    name = models.CharField("Intitulé", max_length=50, default="")
    email = models.CharField("Adresse email", max_length=100, default="", blank=True)
    phone = models.CharField("Téléphone", max_length=100, default="", blank=True)
    address = models.CharField("Adresse", max_length=100, default="", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Prestataire"
        verbose_name_plural = "Prestataires"
        ordering = ("-createdAt",)

    def __str__(self):
        return self.name
