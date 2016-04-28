# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_id', models.TextField()),
                ('name', models.TextField()),
                ('sex', models.TextField()),
                ('age', models.TextField()),
                ('contact_email', models.TextField()),
                ('contact_phone', models.TextField()),
                ('city', models.TextField()),
                ('zip_code', models.TextField()),
                ('size', models.TextField()),
                ('description', models.TextField()),
                ('breeds', models.ManyToManyField(to='dogs.Breed')),
            ],
        ),
    ]
