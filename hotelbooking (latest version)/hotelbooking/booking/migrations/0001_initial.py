# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-25 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('bsdate', models.DateField()),
                ('b_daysno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking_has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cust_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('add', models.CharField(default='', max_length=500)),
                ('email', models.CharField(max_length=100)),
                ('country', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('title', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room_types',
            fields=[
                ('rt_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=50)),
                ('maxno', models.CharField(max_length=10)),
                ('b_price', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=10)),
                ('bed_no', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=10)),
                ('boat', models.CharField(max_length=10)),
                ('parking', models.CharField(max_length=10)),
                ('library', models.CharField(max_length=10)),
                ('cinema', models.CharField(max_length=10)),
                ('plift', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=100)),
                ('bld', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('r_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('floor', models.CharField(max_length=10)),
                ('rt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Room_types')),
            ],
        ),
        migrations.AddField(
            model_name='booking_has',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Cust_info'),
        ),
        migrations.AddField(
            model_name='booking_has',
            name='r_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Rooms'),
        ),
        migrations.AlterUniqueTogether(
            name='booking_has',
            unique_together=set([('b_id', 'r_id', 'c_id')]),
        ),
    ]
