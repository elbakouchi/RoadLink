# Generated by Django 3.2.12 on 2022-04-03 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20220402_1918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='budget',
            options={'ordering': ('-createdAt',), 'verbose_name': 'Budget', 'verbose_name_plural': 'Budgets'},
        ),
        migrations.AddField(
            model_name='budget',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='budget',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
