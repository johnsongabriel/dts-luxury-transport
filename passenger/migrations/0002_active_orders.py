# Generated by Django 4.0 on 2023-03-26 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=50)),
                ('billing_status', models.BooleanField(default=False)),
                ('order_key', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Active Orders',
                'verbose_name_plural': 'Active Orders',
                'ordering': ['-date'],
            },
        ),
    ]
