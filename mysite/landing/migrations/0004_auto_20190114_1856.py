# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-14 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20190113_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'MySubscriber', 'verbose_name_plural': 'A lot of subsribers'},
        ),
    ]
