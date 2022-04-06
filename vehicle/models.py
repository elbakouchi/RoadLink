from django.db import models
from django.contrib.auth.models import User


class Parking(models.Model):
    name = models.CharField("Intitulé", default="", max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Parc %s" % self.name

    class Meta:
        verbose_name = "Parc"
        verbose_name_plural = "Parcs"
        ordering = ("-createdAt",)


class Vehicle(models.Model):
    VEHICLE_STATUS_CHOICES = (
        ('B', 'En mission'),
        ('NB', 'Dans le parc'),
        ('NB', 'En panne'),
        ('R', 'En réparation'),
        ('A', 'Autre'),
    )
    INSURANCE_STATUS_CHOICES = (
        ('U', 'A jour'),
        ('NU', 'Hors échéance'),
    )
    VEHICLE_TYPE_CHOICES = (
        ('P', 'Utilitaire'),
        ('T', 'Luxe'),
        ('C', 'Poids lourd'),
        ('G', 'Agricole'),
        ('M', 'Autre'),
    )
    FUEL_TYPE_CHOICES = (
        ('D', 'Diesel'),
        ('G', 'Essence'),
        ('E', 'Eléctrique'),
        ('H', 'Hybride')
    )
    brand = models.CharField("Marque", max_length=50, default="Dacia")
    model = models.CharField("Modèle", max_length=50, default="Logan")
    registration_plate = models.CharField("Matricule", max_length=200, default='')
    parking = models.ForeignKey(Parking, default=None, null=True, on_delete=models.CASCADE, verbose_name="Parc")
    vehicle_status = models.CharField("État du véhicule", max_length=2, default='NB', choices=VEHICLE_STATUS_CHOICES)
    insurance_status = models.CharField("Assurance", max_length=2, default='U', choices=INSURANCE_STATUS_CHOICES)
    # no_of_km_travelled = models.DecimalField(max_digits=20, default=0, decimal_places=0)
    fuel_type = models.CharField("Type carburant", max_length=1, default='P', choices=FUEL_TYPE_CHOICES)
    mileage = models.DecimalField("Kilométrage", max_digits=20, default=0, decimal_places=0, blank=True)
    vehicle_type = models.CharField("Type de véhicule", max_length=1, default='P', choices=VEHICLE_TYPE_CHOICES)
    image = models.ImageField(upload_to="vehicle_image", default="default.png", blank=True)
    # owner = models.ForeignKey(User, default=None, blank=True, verbose_name="Propriètaire")
    # cost_per_km = models.DecimalField("Consommation par kilomètre", max_digits=20, default=0, decimal_places=2,
    #                                  blank=True)
    # price = models.DecimalField('Prix', max_digits=20, default="0", decimal_places=3, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
        ordering = ("-createdAt",)

    def __str__(self):
        return "%s - %s %s" % (self.registration_plate, self.brand, self.model)
