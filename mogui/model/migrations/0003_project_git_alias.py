# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git_alias',
            field=models.CharField(default='', max_length=60, verbose_name='git\u522b\u540d'),
        ),
    ]
