# Generated by Django 3.2.12 on 2022-12-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_appointment_is_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='patient_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_surname',
            field=models.CharField(default='kalimbekova', max_length=60),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(default='aidand', max_length=60),
        ),
    ]
