# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=20)
    passphrase = models.CharField(max_length=100)

    def __unicode__(self): # pragma: no cover
        return self.username

class Patient(models.Model):
    name = models.CharField(max_length=45)
    patient = models.ForeignKey('User')

    def __unicode__(self):  # pragma: no cover
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=45)
    doctor = models.ForeignKey('User')

    def __unicode__(self): # pragma: no cover
        return self.name

class Prediction(models.Model):
    patient = models.ForeignKey('Patient')
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self): # pragma: no cover
        return u'%s %s' % (self.patient, self.date)

class Logit(models.Model):
    prediction = models.ForeignKey('Prediction') #many_too_one relationship

    def __unicode__(self): # pragma: no cover
        return self.prediction

class HazardFunction(models.Model):
    prediction = models.ForeignKey('Prediction')

    def __unicode__(self):  # pragma: no cover
        return u'%s %s' % (self.prediction, self.factors)

class ExpectancyData(models.Model):
    hazard = models.ForeignKey('HazardFunction')
    percentage_survival = models.DecimalField(max_digits=6,decimal_places=3)
    num_weeks = models.IntegerField()

    def __unicode__(self): # pragma: no cover
        return u'%s %s' % (self.num_weeks, self.percentage_survival)

class MutatedGenes(models.Model):
    gene_name = models.CharField(max_length=45)
    meth_score = models.DecimalField(max_digits=4,decimal_places=3)
    logit = models.ForeignKey('Logit') #many_to_one relationship

    def __unicode__(self): # pragma: no cover
        return u'%s %s' % (self.gene_name, self.meth_score)

class SurvivalFactors(models.Model):
    logit = models.ForeignKey('Logit')
    hazard = models.ForeignKey('HazardFunction')


