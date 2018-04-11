# Generated by Django 2.0.4 on 2018-04-11 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180406_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='latitude',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
        migrations.AddField(
            model_name='book',
            name='longitude',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
    ]
