# Generated by Django 4.2.11 on 2024-04-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
