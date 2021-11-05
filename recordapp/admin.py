from django.contrib import admin
from .models import Patient_info, patient_pic, Rank, Next_of_kin, Address

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('hospitalNo', 'surname', 'othernames', 'data_of_birth', 'sex', 'email')
    
admin.site.register(Patient_info, PatientAdmin)
class PatientPic(admin.ModelAdmin):
    pass
admin.site.register(patient_pic, PatientPic)

admin.site.register(Rank)
admin.site.register(Address)
admin.site.register(Next_of_kin)