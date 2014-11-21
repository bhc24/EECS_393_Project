from django.contrib import admin
from pamlla.models import Patient, User, Doctor, Prediction, Logit, HazardFunction, ExpectancyData, MutatedGenes, SurvivalFactors
# Register your models here.
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Prediction)
admin.site.register(Logit)
admin.site.register(HazardFunction)
admin.site.register(ExpectancyData)
admin.site.register(MutatedGenes)
admin.site.register(SurvivalFactors)