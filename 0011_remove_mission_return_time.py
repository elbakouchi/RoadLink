# Generated by Django 3.2.12 on 2022-04-10 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0010_alter_mission_return_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='return_time',
        ),
    ]
