# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-03 18:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicusers', '0003_auto_20170703_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 3, 18, 0, 54, 672855, tzinfo=utc)),
        ),
    ]
