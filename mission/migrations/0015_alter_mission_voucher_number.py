# Generated by Django 3.2.12 on 2022-05-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0014_alter_mission_voucher_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='voucher_number',
            field=models.PositiveIntegerField(default='', verbose_name='N° Bon'),
        ),
    ]
