# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parkir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=50, verbose_name=b'ID Card')),
                ('gate', models.PositiveSmallIntegerField(choices=[(0, b'GATE1'), (1, b'GATE2')], default=0, verbose_name=b'Gate')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, b'CHECKIN'), (1, b'CHECKOUT')], default=0, verbose_name=b'Status')),
                ('tanggal', models.DateField(verbose_name=b'tanggal')),
                ('jam', models.TimeField(verbose_name=b'jam')),
                ('biaya', models.IntegerField(verbose_name=b'biaya')),
            ],
            options={
                'verbose_name': 'Parkir',
            },
        ),
    ]
