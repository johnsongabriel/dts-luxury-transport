# Generated by Django 4.0 on 2023-03-16 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0002_remove_subcriber_conf_num_alter_subcriber_confirmed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcriber',
            options={'verbose_name': 'Subcribe', 'verbose_name_plural': 'Subcribes'},
        ),
    ]