# Generated by Django 4.1.1 on 2023-03-20 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passenger", "0005_bookingdb_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookingdb",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
