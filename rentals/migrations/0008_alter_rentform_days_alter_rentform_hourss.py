# Generated by Django 4.1.1 on 2023-03-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0007_alter_rentform_car_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentform",
            name="Days",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="rentform",
            name="hourss",
            field=models.CharField(max_length=20),
        ),
    ]