# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0003_auto_20170415_1430'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together=set([('userinfo', 'product')]),
        ),
    ]
