# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_has',
            name='b_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
        ),
    ]
