# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_profile_games_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='games_liked',
            field=models.ManyToManyField(to='app.Game'),
        ),
    ]