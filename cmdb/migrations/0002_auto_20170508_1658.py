# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostinfo',
            old_name='userId',
            new_name='user',
        ),
    ]
