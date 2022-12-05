from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit


class Patient(models.Model):
    class BLOOD_GROUP(models.TextChoices):
        A = "A"
        B = "B"
        O = "O"
        AB = "AB"

    class MARITAL_STATUS(models.TextChoices):
        SINGLE = "s"
        MARRIED = "m"
        DIVORCED = "d"

    birth_date = models.DateField("Birth Date", null=True)
    iin = models.CharField("IIN", max_length=14)
    patient_id = models.PositiveIntegerField("Patient ID", default=0)
    name = models.CharField("Name", max_length=32)
    surname = models.CharField("Surname", max_length=32)
    middle_name = models.CharField("Middle name", max_length=32, blank=True)
    blood_group = models.CharField(
        "Blood Group", max_length=2, choices=BLOOD_GROUP.choices
    )
    # emergency_contact_number = models.CharField(
    #     "Emergency Contact Number", max_length=12
    # )
    contact_number = models.CharField("Contact Number", max_length=12)
    email = models.EmailField(("Email"), blank=True, null=True, unique=True)
    address = models.CharField("Address", max_length=64)
    marital_status = models.CharField("Marital Status", max_length=1, choices=MARITAL_STATUS.choices)
    registration_date = models.DateField("Registration Field", null=True)


class Doctor(models.Model):
    class CATEGORY(models.IntegerChoices):
        HIGEST = 0
        FIRST = 1
        SECOND = 2

    class EDUCATION(models.TextChoices):
        MD = "MD"
        PHD = "PHD"

    birth_date = models.DateField("Birth Date", null=True)
    iin = models.CharField("IIN", max_length=12)
    doctor_id = models.PositiveIntegerField("Doctor ID", default=0)
    name = models.CharField("Name", max_length=32)
    surname = models.CharField("Surname", max_length=32)
    middle_name = models.CharField("Middle name", max_length=32, blank=True)
    department_id = models.PositiveIntegerField("Department ID", default=0)
    specialization_id = models.PositiveIntegerField("Specialization ID", default=0)
    experience = models.PositiveIntegerField("Experience in Years", default=0)
    photo = ProcessedImageField(
        verbose_name="Photo",
        upload_to="doctor/photos/",
        null=True,
        blank=True,
        format="JPEG",
        options={"quality": 90},
        processors=[
            ResizeToFit(width=1920, height=1200, upscale=False),  # max-width
        ],
    )
    category = models.PositiveSmallIntegerField("Category", choices=CATEGORY.choices)
    price = models.PositiveIntegerField("Price of Appointment", default=0)
    schedule_details = models.CharField("Schedule Details", max_length=256)
    education = models.CharField("Education", max_length=3, choices=EDUCATION.choices)
    rating = models.PositiveSmallIntegerField("Rating", default=0)
    address = models.CharField("Address", max_length=64)
    speciality = models.CharField("Speciality", max_length=30, default='some speciality')

    def __str__(self):
        return '{} {}'.format(self.speciality, self.short_name)
    @property
    def short_name(self):
        return '{} {} {} '.format(self.name, self.middle_name, self.surname)


class Appointment(models.Model):

    class Meta:
        unique_together = ('doctor', 'date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '09:00 - 09:30'),
        (1, '10:00 - 10:30'),
        (2, '11:00 - 11:30'),
        (3, '12:00 - 12:30'),
        (4, '13:00 - 13:30'),
        (5, '14:00 - 14:30'),
        (6, '15:00 - 15:30'),
        (7, '16:00 - 16:30'),
        (8, '17:00 - 17:30'),
    )

    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, related_name='timeslots')
    date = models.DateField(help_text="DD-MM-YYYY")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    patient_name = models.CharField(max_length=60, default = "aidand")
    patient_surname = models.CharField(max_length=60, default = "kalimbekova")
    patient_email = models.EmailField(("Email"), blank=True, null=True)

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.date, self.time, self.doctor, self.patient_name)

    @property
    def time(self):
        return self.TIMESLOT_LIST[self.timeslot][1]

