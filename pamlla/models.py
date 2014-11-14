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

class ExpectancyData(models.Model):
	prediction = models.ForeignKey('Prediction')
	percentage_survival = models.IntegerField()
	num_weeks = models.IntegerField()

class DocToPatient(models.Model):
	doctor_id = models.ForeignKey('Doctor')
	patient_id = models.ForeignKey('Patient')
