# Generated by Django 4.0 on 2023-03-16 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_details', models.CharField(max_length=50)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time_hour', models.CharField(max_length=100)),
                ('pick_up_time_mins', models.CharField(max_length=100)),
                ('number_of_passenger', models.IntegerField()),
                ('number_of_luggages', models.IntegerField()),
                ('pick_up_address', models.CharField(blank=True, max_length=150, null=True)),
                ('dropoff_address', models.CharField(blank=True, max_length=150, null=True)),
                ('dropoff_airport', models.CharField(blank=True, max_length=150, null=True)),
                ('pickup_airport', models.CharField(blank=True, max_length=150, null=True)),
                ('distance', models.CharField(max_length=150, null=True)),
                ('way_point_1', models.CharField(blank=True, max_length=250)),
                ('way_point_2', models.CharField(blank=True, max_length=250)),
                ('airline', models.CharField(max_length=200)),
                ('work_hour', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_number', models.CharField(blank=True, max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ContactFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=400)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subcriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('confirmed', models.BooleanField(default=False)),
                ('conf_num', models.CharField(max_length=15)),
            ],
        ),
    ]
