# Generated by Django 3.2.12 on 2022-05-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0011_alter_mission_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='provider',
        ),
        migrations.AlterField(
            model_name='mission',
            name='voucher_number',
            field=models.PositiveIntegerField(default='', max_length=50, verbose_name='N° Bon'),
        ),
    ]
