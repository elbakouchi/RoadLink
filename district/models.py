from django.db import models
from datetime import datetime


class District(models.Model):
    name = models.CharField("Intitulé", default="", max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Division"
        verbose_name_plural = "Divisions"
        ordering = ("-createdAt",)
