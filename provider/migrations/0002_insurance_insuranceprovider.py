# Generated by Django 3.2.12 on 2022-05-14 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Intitulé')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Assureur',
                'verbose_name_plural': 'Assureur',
                'ordering': ('-createdAt',),
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField(blank=True)),
                ('endDate', models.DateField(blank=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('provider', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='provider.insuranceprovider', verbose_name='Assureur')),
                ('vehicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle', verbose_name='Véhicule')),
            ],
            options={
                'verbose_name': 'Assurance',
                'verbose_name_plural': 'Assurances',
                'ordering': ('-createdAt',),
            },
        ),
    ]
