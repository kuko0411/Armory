# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_auto_20170405_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.ItemData'),
        ),
    ]