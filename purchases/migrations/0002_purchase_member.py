# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('purchases', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Member'),
        ),
    ]
