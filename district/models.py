from django.db import models


class District(models.Model):
    name = models.CharField("Intitulé", default="", max_length=100)

