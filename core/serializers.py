from rest_framework import serializers
from .models import Doctor, Patient, Appointment
#from drf_spectacular.utils import extend_schema_field

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
    
class AppointmentShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ["date", "timeslot"]

class DoctorAppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name", "surname", "speciality"]