# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-09-02 15:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20180812_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 2, 15, 14, 29, 970825, tzinfo=utc)),
        ),
    ]
