# Generated by Django 3.2.12 on 2022-04-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('fiscal_year', models.DateField(verbose_name='Exercice')),
                ('amount', models.FloatField(verbose_name='Montant')),
            ],
        ),
    ]
