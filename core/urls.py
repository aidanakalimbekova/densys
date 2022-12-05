from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, AppointmentListAPIView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'appointments', AppointmentViewSet, basename='appointments')
#router.register(r'doctor_appointments', AppointmentListAPIView.as_view(), basename='doctor_appointments')
#router.register(r'book_appointment', DoctorAppointViewSet, basename='book_appointment')
urlpatterns = [
    path('', include(router.urls)),
    path('appointment-timeslots/', AppointmentListAPIView.as_view(), 
         name='appointment-timeslots'),
]