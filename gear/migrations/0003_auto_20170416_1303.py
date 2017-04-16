# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gear', '0002_auto_20170414_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear_item',
            name='slot',
            field=models.IntegerField(choices=[('Weapon', 1), ('Armor', 3), ('Gloves', 4), ('Boots', 5), ('Left earing', 6), ('Right earing', 7), ('Left ring', 8), ('Right ring', 9), ('Necklace', 10), ('Innerwear', 11), ('Belt', 19), ('Brooch', 20)]),
        ),
    ]