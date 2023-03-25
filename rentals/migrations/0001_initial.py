# Generated by Django 4.0 on 2023-03-25 21:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_rent_img', models.ImageField(upload_to='rents/')),
                ('car_rent_img_1', models.ImageField(upload_to='rents/')),
                ('car_rent_img_2', models.ImageField(upload_to='rents/')),
                ('car_rent_img_3', models.ImageField(upload_to='rents/')),
                ('car_rent_img_4', models.ImageField(upload_to='rents/')),
                ('car_rent_img_5', models.ImageField(upload_to='rents/')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Rents',
                'verbose_name_plural': 'Rents',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='RentForm',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('car_id', models.CharField(max_length=60)),
                ('user_id', models.CharField(editable=False, max_length=60)),
                ('user_names', models.CharField(max_length=60)),
                ('email_user', models.EmailField(max_length=100)),
                ('hourss', models.CharField(max_length=15)),
                ('Days', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('total', models.IntegerField(blank=True, null=True)),
                ('car_rent_name', models.CharField(max_length=50)),
                ('car_rent_model', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ordered', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Rents Form',
                'verbose_name_plural': 'Rents Form',
                'ordering': ['-date'],
            },
        ),
    ]
