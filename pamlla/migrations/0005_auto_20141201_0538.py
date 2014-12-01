# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pamlla', '0004_auto_20141201_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='mutatedgenes',
            name='coefficient_value',
            field=models.DecimalField(default=1.0, max_digits=7, decimal_places=5),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mutatedgenes',
            name='data_type',
            field=models.CharField(default=b'Unknown', max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default='Filler Name', max_length=30),
            preserve_default=False,
        ),
    ]
