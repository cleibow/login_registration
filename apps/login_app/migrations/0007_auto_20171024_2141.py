# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_auto_20171024_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 10, 24, 21, 41, 16, 478512), verbose_name='YYYY-MM-DD'),
        ),
    ]
