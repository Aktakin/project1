# Generated by Django 4.1.7 on 2023-03-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_patient_id_vital_signs_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vital_signs',
            name='date',
            field=models.DateTimeField(default='2022-02-12 23:34', null=True),
        ),
    ]
