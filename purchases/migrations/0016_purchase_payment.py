# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 22:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('purchases', '0015_auto_20170412_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.Payment'),
        ),
    ]
