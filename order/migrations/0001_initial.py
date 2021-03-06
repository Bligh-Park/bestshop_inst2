# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery_fee', models.IntegerField()),
                ('point', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('tid', models.CharField(max_length=128)),
                ('state', models.IntegerField()),
                ('postcode', models.CharField(max_length=5)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=64)),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('point', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
