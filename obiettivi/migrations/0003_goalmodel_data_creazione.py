# Generated by Django 4.1.7 on 2023-05-27 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('obiettivi', '0002_remove_goalmodel_is_completed_goalmodel_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalmodel',
            name='data_creazione',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
