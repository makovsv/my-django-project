# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-26 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_quest', '0003_auto_20190126_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeprofile',
            name='gender',
            field=models.BooleanField(),
        ),
    ]
