# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(default='')),
                ('favorites', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dogs.Dog')),
            ],
        ),
    ]
