# Generated by Django 4.1.1 on 2023-03-20 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("passenger", "0003_alter_bookingdb_guess_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookingdb",
            old_name="guess_id",
            new_name="booking_id",
        ),
    ]
