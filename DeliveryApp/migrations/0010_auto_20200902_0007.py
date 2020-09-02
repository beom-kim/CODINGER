# Generated by Django 3.1 on 2020-09-01 15:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryApp', '0009_auto_20200901_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryinfo',
            name='menuList',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuList2', to='DeliveryApp.menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='optionList',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='optionList', to='DeliveryApp.option'),
        ),
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.TimeField(default=datetime.datetime(2020, 9, 2, 0, 7, 15, 63561)),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveryTime',
            field=models.TimeField(default=datetime.datetime(2020, 9, 2, 0, 7, 15, 62670)),
        ),
        migrations.AlterField(
            model_name='store',
            name='deliveryPriceList',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DeliveryApp.deliveryprice'),
        ),
        migrations.AlterField(
            model_name='store',
            name='menuList',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menuList', to='DeliveryApp.menu'),
        ),
    ]