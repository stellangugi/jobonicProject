# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicusers', '0005_auto_20170705_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
