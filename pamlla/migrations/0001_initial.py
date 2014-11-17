# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExpectancyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percentage_survival', models.DecimalField(max_digits=6, decimal_places=3)),
                ('num_weeks', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HazardFunction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Logit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MutatedGenes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gene_name', models.CharField(max_length=45)),
                ('meth_score', models.DecimalField(max_digits=4, decimal_places=3)),
                ('logit', models.ForeignKey(to='pamlla.Logit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patient', models.ForeignKey(to='pamlla.Patient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SurvivalFactors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hazard', models.ForeignKey(to='pamlla.HazardFunction')),
                ('logit', models.ForeignKey(to='pamlla.Logit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('passphrase', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient',
            field=models.ForeignKey(to='pamlla.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logit',
            name='prediction',
            field=models.ForeignKey(to='pamlla.Prediction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hazardfunction',
            name='factors',
            field=models.ForeignKey(to='pamlla.SurvivalFactors'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hazardfunction',
            name='prediction',
            field=models.ForeignKey(to='pamlla.Prediction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='expectancydata',
            name='hazard',
            field=models.ForeignKey(to='pamlla.HazardFunction'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor',
            field=models.ForeignKey(to='pamlla.User'),
            preserve_default=True,
        ),
    ]
