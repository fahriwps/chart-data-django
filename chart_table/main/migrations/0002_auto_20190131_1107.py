# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkir',
            name='biaya',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'biaya'),
        ),
    ]
