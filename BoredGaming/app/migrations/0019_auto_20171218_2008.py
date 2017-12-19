# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20171218_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='games_liked',
            field=models.ManyToManyField(related_name='liked', to='app.Game'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='games_owned',
            field=models.ManyToManyField(related_name='owned', to='app.Game'),
        ),
    ]
