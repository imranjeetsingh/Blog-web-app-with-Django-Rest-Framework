# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-23 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190320_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='read_time',
            field=models.IntegerField(default=0),
        ),
    ]
