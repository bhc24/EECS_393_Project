# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pamlla', '0006_patient_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'documents')),
                ('prediction', models.ForeignKey(to='pamlla.Prediction')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='isDoctor',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='isPatient',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
