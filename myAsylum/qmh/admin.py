from django.contrib import admin
from qmh.models import *
from django.contrib.flatpages.models import FlatPage

#Note: We are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from import_export.admin import ImportExportModelAdmin
from .models import Patient


# Flatpages section
class FlatpageForm(FlatpageFormOld):
  content = forms.CharField(widget=CKEditorUploadingWidget())
  class Meta:
    model = FlatPage # this is not automatically inherited from FlatpageFormOld
    fields = '__all__'
    
class FlatPageAdmin(FlatPageAdminOld):
  form = FlatpageForm
  
#We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)


# Register your models here.



class PatientAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Patient, PatientAdmin)
