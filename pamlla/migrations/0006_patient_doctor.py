# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pamlla', '0005_auto_20141201_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=0, to='pamlla.Doctor'),
            preserve_default=False,
        ),
    ]
