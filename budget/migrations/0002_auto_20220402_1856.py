# Generated by Django 3.2.12 on 2022-04-02 18:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='fiscal_year',
        ),
        migrations.AddField(
            model_name='budget',
            name='fiscal_year_end',
            field=models.DateField(default=datetime.datetime(2022, 4, 2, 18, 56, 12, 298544, tzinfo=utc), verbose_name="Date fin d'exercice"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='budget',
            name='fiscal_year_start',
            field=models.DateField(default=datetime.datetime(2022, 4, 2, 18, 56, 23, 774, tzinfo=utc), verbose_name="Date début d'exercice"),
            preserve_default=False,
        ),
    ]
