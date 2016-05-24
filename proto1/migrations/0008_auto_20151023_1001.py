# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proto1', '0007_auto_20151023_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expectedfamilycontribution',
            name='expected_family_contribution',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='expectedfamilycontribution',
            name='family_income',
            field=models.IntegerField(),
        ),
    ]
