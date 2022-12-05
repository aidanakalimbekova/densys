# Generated by Django 3.2.12 on 2022-12-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_patient_patient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='emergency_contact_number',
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.PositiveIntegerField(default=0, verbose_name='Patient ID'),
        ),
    ]
