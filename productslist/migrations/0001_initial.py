# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=20)),
                ('openPrice', models.FloatField()),
                ('closePrice', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
