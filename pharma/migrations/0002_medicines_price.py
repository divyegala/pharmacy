# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-03-23 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicines',
            name='price',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
