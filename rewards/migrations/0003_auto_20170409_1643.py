# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 08:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0002_auto_20170408_1614'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reward',
            options={'ordering': ('award_datetime',)},
        ),
        migrations.AddField(
            model_name='reward',
            name='check',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reward',
            name='award_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='reward',
            name='expiry_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today),
        ),
    ]
