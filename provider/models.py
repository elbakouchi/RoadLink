from django.db import models


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
