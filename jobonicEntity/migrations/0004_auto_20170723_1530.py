# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobonicEntity', '0003_entity_entity_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='url',
        ),
        migrations.AlterField(
            model_name='entityprofile',
            name='facebook',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='entityprofile',
            name='linkedIn',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='entityprofile',
            name='twitter',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='entityprofile',
            name='url',
            field=models.CharField(max_length=70),
        ),
    ]
