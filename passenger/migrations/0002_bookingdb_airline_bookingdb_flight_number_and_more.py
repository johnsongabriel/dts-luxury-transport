# Generated by Django 4.1.1 on 2023-03-02 23:27

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("passenger", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingdb",
            name="airline",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="bookingdb",
            name="flight_number",
            field=models.IntegerField(
                default=1000
                #default=datetime.datetime(
                #    2023, 3, 2, 23, 27, 48, 593126, tzinfo=datetime.timezone.utc
                #)
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bookingdb",
            name="drop_off_address",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="bookingdb",
            name="pick_up_address",
            field=models.CharField(max_length=150),
        ),
    ]
