# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20180723_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='last_check',
            field=models.DateTimeField(auto_now=True, db_index=True, help_text='检测时间', verbose_name='检测时间'),
        ),
    ]
