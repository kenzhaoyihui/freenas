# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-11 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vm', '0002_auto_20170504_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm',
            name='autostart',
            field=models.BooleanField(default=True, help_text='Guest VM will start on boot.', verbose_name='Autostart'),
        ),
    ]