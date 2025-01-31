# Generated by Django 3.2.12 on 2022-04-03 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ('-createdAt',), 'verbose_name': 'Division', 'verbose_name_plural': 'Divisions'},
        ),
        migrations.AddField(
            model_name='district',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
