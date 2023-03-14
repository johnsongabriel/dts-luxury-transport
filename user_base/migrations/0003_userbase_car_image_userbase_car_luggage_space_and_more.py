# Generated by Django 4.1.1 on 2023-03-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_base", "0002_userbase_last_name_alter_userbase_is_driver"),
    ]

    operations = [
        migrations.AddField(
            model_name="userbase",
            name="car_image",
            field=models.ImageField(default="default.jpg", upload_to="images/cars/"),
        ),
        migrations.AddField(
            model_name="userbase",
            name="car_luggage_space",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="userbase",
            name="car_name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="userbase",
            name="car_seats",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]