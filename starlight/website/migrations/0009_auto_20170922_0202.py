# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-22 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20170920_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='photo_isFavourite',
            new_name='photo_is_favourite',
        ),
    ]
