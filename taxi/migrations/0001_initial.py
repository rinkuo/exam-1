# Generated by Django 5.1.3 on 2024-11-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxi_name', models.CharField(max_length=100)),
                ('license_plate', models.PositiveIntegerField()),
                ('driver_name', models.CharField(max_length=100)),
                ('passenger_capacity', models.PositiveIntegerField()),
                ('car_model', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
