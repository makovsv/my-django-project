# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-14 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life_quest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifeprofile',
            name='smoking',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
