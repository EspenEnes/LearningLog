# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningLogs', '0003_topic_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
