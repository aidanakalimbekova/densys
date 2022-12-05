from core.models import Doctor, Patient, Appointment
from django.contrib import admin

# Register your models here.



class PatientAdmin(admin.ModelAdmin):
    list = ('birth_date', 'iin', 'patient_id', 'name', 'surname', 'middle_name', 'blood_group', 'emergency_contact_number', 'contact_number', 'email', 'address', 'marital_status', 'registration_date')

admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list = ('birth_date', 'iin', 'doctor_id', 'name', 'surname', 'middle_name', 'department_id', 'specialization_id', 'experience', 'photo', 'category', 'price', 'schedule_details', 'education', 'rating', 'address')

admin.site.register(Doctor, DoctorAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'timeslot', 'patient_name']
    list_filter = ['doctor', ]

admin.site.register(Appointment, AppointmentAdmin)