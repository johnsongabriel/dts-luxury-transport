# Generated by Django 4.0 on 2023-03-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_detail', models.CharField(max_length=50)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('number_of_passenger', models.IntegerField()),
                ('number_of_luggages', models.IntegerField()),
                ('pick_up_address', models.CharField(max_length=100)),
                ('drop_off_address', models.CharField(max_length=100)),
            ],
        ),
    ]
