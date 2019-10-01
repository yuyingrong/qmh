from django.contrib import admin
from qmh.models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)