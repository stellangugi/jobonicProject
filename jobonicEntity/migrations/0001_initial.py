# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.URLField()),
                ('about_company', models.TextField()),
                ('facebook', models.CharField(max_length=50)),
                ('linkedIn', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('date_established', models.DateField()),
                ('tags', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]