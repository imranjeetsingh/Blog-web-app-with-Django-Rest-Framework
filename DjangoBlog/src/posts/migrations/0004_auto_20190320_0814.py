# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-20 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190320_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publsih',
            new_name='publish',
        ),
    ]
