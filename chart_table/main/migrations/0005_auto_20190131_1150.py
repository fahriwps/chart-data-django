# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190131_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkir',
            name='biaya',
            field=models.IntegerField(blank=True, choices=[(1000, 1000), (2000, 2000), (3000, 3000), (4000, 4000), (5000, 5000), (6000, 6000), (7000, 7000), (8000, 8000), (9000, 9000), (10000, 10000)], null=True, verbose_name=b'biaya'),
        ),
    ]
