from django.db import models
from vehicle.models import Vehicle
from django_q.tasks import async_task


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


class GasSupplier(Provider):
    class Meta:
        verbose_name = "Distributeur Carburant"
        verbose_name_plural = "Distributeurs Carburant"
        ordering = ("-createdAt",)

    def __str__(self):
        return self.name

# Message on object change
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_q.tasks import async_task
from datetime import datetime

# set up the pre_save signal for our user
@receiver(pre_save, sender=Insurance)
def insurance_changed(sender, instance, **kwargs):
    try:
        insurance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # new user
    else:
        today = datetime.date.today()
        delta = insurance.endDate() - today
        if delta <= 7:
            async_task('inform_everyone', instance)


def inform_everyone(user):
    mails = []
    for u in User.objects.exclude(pk=user.pk):
        msg = f"Dear {u.username}, {user.username} has a new email address: {user.email}"
        mails.append(('New email', msg,
                      'from@example.com', [u.email]))
    return send_mass_mail(mails)