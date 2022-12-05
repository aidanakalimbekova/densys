# Generated by Django 3.2.12 on 2022-12-03 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(default='some speciality', max_length=30, verbose_name='Speciality'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='DD-MM-YYYY')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 - 09:30'), (1, '10:00 - 10:30'), (2, '11:00 - 11:30'), (3, '12:00 - 12:30'), (4, '13:00 - 13:30'), (5, '14:00 - 14:30'), (6, '15:00 - 15:30'), (7, '16:00 - 16:30'), (8, '17:00 - 17:30')])),
                ('patient_name', models.CharField(max_length=60)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
            options={
                'unique_together': {('doctor', 'date', 'timeslot')},
            },
        ),
    ]
