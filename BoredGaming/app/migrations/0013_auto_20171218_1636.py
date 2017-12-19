# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20171218_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='games_owned',
        ),
        migrations.AlterField(
            model_name='profile',
            name='games_liked',
            field=models.ManyToManyField(to='app.Game'),
        ),
    ]
