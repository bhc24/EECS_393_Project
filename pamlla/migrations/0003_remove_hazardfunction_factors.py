# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pamlla', '0002_prediction_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hazardfunction',
            name='factors',
        ),
    ]
