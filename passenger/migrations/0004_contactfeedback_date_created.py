# Generated by Django 4.0 on 2023-03-14 00:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0003_contactfeedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactfeedback',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
