# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pamlla', '0003_remove_hazardfunction_factors'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isDoctor', models.BooleanField(default=True)),
                ('isPatient', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor',
            field=models.ForeignKey(to='pamlla.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient',
            field=models.ForeignKey(to='pamlla.UserProfile'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
