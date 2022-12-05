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


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class AppointmentListAPIView(ListAPIView):
    serializer_class = DoctorAppointSerializer
    queryset = Doctor.objects.all()
