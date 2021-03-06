# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# 1. Created OneToOneField between the library User object and our UserProfile model
# 2. Created extra fields: isDoctor and isPatient
# 3. Go to admin.py
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):  # pragma: no cover
        return self.user.username


class Patient(models.Model):
    patient = models.ForeignKey('UserProfile')
    doctor = models.ForeignKey('Doctor')

    def __unicode__(self):
        return self.patient.user.username

class Doctor(models.Model):
    doctor = models.ForeignKey('UserProfile')

class Prediction(models.Model):
    patient = models.ForeignKey('Patient')
    date = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100)

    def __unicode__(self):  # pragma: no cover
        return u'%s %s' % (self.patient, self.date)


class Logit(models.Model):
    prediction = models.ForeignKey('Prediction') #many_too_one relationship

    def __unicode__(self):  # pragma: no cover
        return self.prediction


class HazardFunction(models.Model):
    prediction = models.ForeignKey('Prediction')

    def __unicode__(self):  # pragma: no cover
        return u'%s %s' % (self.prediction, self.factors)


class ExpectancyData(models.Model):
    hazard = models.ForeignKey('HazardFunction')
    percentage_survival = models.DecimalField(max_digits=6,decimal_places=3)
    num_weeks = models.IntegerField()

    def __unicode__(self):  # pragma: no cover
        return u'%s %s' % (self.num_weeks, self.percentage_survival)


class MutatedGenes(models.Model):
    gene_name = models.CharField(max_length=45)
    meth_score = models.DecimalField(max_digits=4,decimal_places=3)
    logit = models.ForeignKey('Logit')  # many_to_one relationship
    data_type = models.CharField(max_length=10, default="Unknown")
    coefficient_value = models.DecimalField(max_digits=7, decimal_places=5, default=1.00000)

    def __unicode__(self):  # pragma: no cover
        return u'%s %s' % (self.gene_name, self.meth_score)


class SurvivalFactors(models.Model):
    logit = models.ForeignKey('Logit')
    hazard = models.ForeignKey('HazardFunction')

class Document(models.Model):

    url = models.CharField(max_length=100)
    # new_url = re.sub("\W+", "", url.lower())

    docfile = models.FileField(upload_to=url)



    # methfile = models.FileField(upload_to='documents')
    # rnafile = models.FileField(upload_to='documents')
