# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotedash', '0003_auto_20180626_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.CharField(max_length=255),
        ),
    ]
