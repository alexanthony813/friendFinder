# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_auto_20160501_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='favorites',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.User'),
        ),
    ]