# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-27 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_quest', '0006_auto_20190127_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifeprofile',
            name='calc_result',
            field=models.IntegerField(default=11),
        ),
    ]
