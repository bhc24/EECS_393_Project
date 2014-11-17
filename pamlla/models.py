# Create your models here.
from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20)
	passphrase = models.CharField(max_length=100)

class Patient(models.Model):
	name = models.CharField(max_length=45)
	patient = models.ForeignKey('User')

class Doctor(models.Model):
	name = models.CharField(max_length=45)
	doctor = models.ForeignKey('User')

class Prediction(models.Model):
	patient = models.ForeignKey('Patient')

class Logit(models.Model):
    prediction = models.ForeignKey('Prediction') #many_too_one relationship

class HazardFunction(models.Model):
    prediction = models.ForeignKey('Prediction')
    factors = models.ForeignKey('SurvivalFactors')

class ExpectancyData(models.Model):
	hazard = models.ForeignKey('HazardFunction')
	percentage_survival = models.DecimalField(max_digits=6,decimal_places=3)
	num_weeks = models.IntegerField()

class MutatedGenes(models.Model):
    gene_name = models.CharField(max_length=45)
    meth_score = models.DecimalField(max_digits=4,decimal_places=3)
    logit = models.ForeignKey('Logit') #many_to_one relationship

class SurvivalFactors(models.Model):
    logit = models.ForeignKey('Logit')
    hazard = models.ForeignKey('HazardFunction')


