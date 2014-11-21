# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pamlla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 3, 3, 51, 136621, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
