# Generated by Django 5.1.1 on 2024-10-10 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kafe', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='date',
        ),
    ]
