# Generated by Django 3.2.12 on 2022-12-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20221204_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='is_booked',
        ),
    ]
