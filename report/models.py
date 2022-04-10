from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Alert(models.Model):
    entity = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name="Entité")
    message = models.CharField(max_length=255, default="")
    object_id = models.PositiveIntegerField(default=None, blank=True, verbose_name="Objet concerné")
    content_object = GenericForeignKey('entity', 'object_id')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alerte"
        verbose_name_plural = "Alertes"
        ordering = ("-createdAt",)

    def __str__(self):
        return f"Intervention {self.vehicle} {self.intervention}"
