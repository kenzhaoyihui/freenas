# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-01 10:34
from __future__ import unicode_literals

from django.db import migrations
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_add_netdata_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsdusers',
            name='bsdusr_attributes',
            field=freenasUI.freeadmin.models.fields.DictField(default=None, editable=False),
        ),
    ]
