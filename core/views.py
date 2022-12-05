# Create your views here.

from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, DoctorAppointSerializer, AppointmentShortSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


# class DoctorAppointViewSet(viewsets.ModelViewSet):
#     serializer_class = AppointmentShortSerializer
#     queryset = Doctor.objects.all()
#     @action(methods=["post"], detail=True)
#     def availableTime(self, request):
#         date = request.data.get('date',"")
#         timeslot = request.data.get('timeslot',"")
#         taken = Appointment.objects.filter(date=date,timeslot=timeslot)
#         taken.is_booked = True
#         taken.save()
#         times = Appointment.objects.get(is_booked=False)
#         times.sort()
#         return Response({'times':times})

    

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentListAPIView(ListAPIView):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentShortSerializer
    def get_queryset(self):
        doctor_id = self.request.query_params.get('doctor', None)
        date = self.request.query_params.get('date', None)
        timeslot = self.request.query_params.get('timeslot', None)

        if doctor_id and date:
            return self.queryset.filter(doctor=doctor_id, date=date)
        
        return self.queryset

    # @action(methods=["get"], detail=True, serializer_class=AppointmentShortSerializer)
    # def choose_time(self, request, *args, **kwargs):
    #     doctor = self.get_object()
    #     appointments = Appointment.objects.filter(doctor_id=doctor.id, is_booked=False)
    #     return Response(data = AppointmentShortSerializer(appointments).data)
    
    # @action(methods=["put"], detail=True, serializer_class=AppointmentShortSerializer)
    # def book_appointment(self, request, *args, **kwargs):
    #     doctor = self.get_object()
    #     date, time = request.data["date"], request.data["time"]
    #     appointment = Appointment.objects.get(doctor_id=doctor.id, date=date, time=time)
    #     appointment.is_booked = True
    #     appointment.save()
    #     return Response(status=status.HTTP_200_OK)