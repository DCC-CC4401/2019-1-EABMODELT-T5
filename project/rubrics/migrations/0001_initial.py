# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('duration_min', models.PositiveSmallIntegerField()),
                ('duration_max', models.PositiveSmallIntegerField()),
                ('state', models.BooleanField()),
            ],
        ),
    ]
