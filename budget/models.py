from django.db import models


class Budget(models.Model):
    title = models.CharField("Titre", max_length=100)
    fiscal_year_start = models.DateField(verbose_name="Date début d'exercice")
    fiscal_year_end = models.DateField(verbose_name="Date fin d'exercice")
    amount = models.FloatField(verbose_name="Montant initial")
    balance = models.FloatField(verbose_name="Balance")
