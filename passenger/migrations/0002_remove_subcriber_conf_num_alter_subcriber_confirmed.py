# Generated by Django 4.0 on 2023-03-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcriber',
            name='conf_num',
        ),
        migrations.AlterField(
            model_name='subcriber',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
    ]