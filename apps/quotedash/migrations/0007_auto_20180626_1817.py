# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotedash', '0006_auto_20180626_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='likecount',
            field=models.IntegerField(null=True),
        ),
    ]
