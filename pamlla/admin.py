from django.contrib import admin
from pamlla.models import Patient, UserProfile, Doctor, Prediction, Logit, HazardFunction, ExpectancyData, MutatedGenes, SurvivalFactors
# Register your models here.
admin.site.register(Patient)
# 1. Changed from User to UserProfile, changed imports as well
# 2. Go to forms.py
admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(Prediction)
admin.site.register(Logit)
admin.site.register(HazardFunction)
admin.site.register(ExpectancyData)
admin.site.register(MutatedGenes)
admin.site.register(SurvivalFactors)