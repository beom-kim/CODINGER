# Generated by Django 3.1 on 2020-09-01 14:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0003_auto_20200901_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.TimeField(default=datetime.datetime(2020, 9, 1, 23, 3, 54, 815662)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryTime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 1, 23, 3, 54, 815662)),
        ),
    ]