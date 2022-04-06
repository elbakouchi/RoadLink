from django.db import models


class Organism(models.Model):
    ministry = models.CharField("Ministère de tutelle", max_length=50, default="Ministère de l'intérieur", blank=True)
    province = models.CharField("Province", max_length=50, default="", blank=True)
    department = models.CharField("Département", max_length=70, default="", blank=True)
    service = models.CharField("Service", max_length=50, default="", blank=True)
    telephone = models.CharField("Téléphone", max_length=15, default="", blank=True)
    address = models.CharField("Adresse", max_length=200, default="", blank=True)
    description = models.TextField("Description", default="", blank=True)
    logo = models.ImageField(upload_to="vehicle_image", default="default.png", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Organisme"
        verbose_name_plural = "Organismes"
        ordering = ("-createdAt",)

    def __str__(self):
        return "%s  %s  %s" % (self.province, self.department, self.service)
