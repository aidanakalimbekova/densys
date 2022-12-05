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
    timeslots = AppointmentSerializer(many=True)
    # name = serializers.SerializerMethodField()

    # def get_name(self, appointment):
    #     return appointment.doctor.name

    # surname = serializers.SerializerMethodField()

    # def get_surname(self, appointment):
    #     return appointment.doctor.surname
   
    # speciality = serializers.SerializerMethodField()

    # def get_speciality(self, appointment):
    #     return appointment.doctor.speciality
    
    class Meta:
        
        fields = ["name", "surname", "speciality", "timeslots"]
        model = Doctor

    # def create(self, validated_data):
    #     data = validated_data.pop("timeslots")
    #     doctor = Doctor.objects.create(**validated_data)
    #     for d in data:
    #         Appointment.objects.create(doctor_id=doctor.id, date=d['date'], timeslot=d['timeslot'], 
    #         patient_name = d['patient_name'], patient_surname = d['patient_surname'], patient_email = d['patient_email'])
    #     return doctor

    #  def update(self, instance, validated_data):
    #     doctor = Doctor.objects.create(**validated_data)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance  
