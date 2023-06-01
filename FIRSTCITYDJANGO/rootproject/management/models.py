from django.db import models

# Create your models here.


class Drug(models.Model):
    name = models.CharField(max_length=255)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.name



class Vital_signs(models.Model):
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    respiratory = models.IntegerField()
    pulse_rate = models.IntegerField()
    blood_pressure = models.IntegerField()
    spo2 = models.IntegerField()
    pre_consultion_action = models.TextField()


class Doctor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Patient(models.Model):



    GENDER_CHOICES = [
        {'Male', 'M'},
        {'Female', 'F'},
    ]

    MARITAL_STATUS = [
        {'single', 'Single'},
        {'married', 'Married'},
        {'divorced', 'Divorced'}
    ]




    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Middle_name = models.CharField(max_length=255)
    address = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)
    next_of_kin = models.CharField(max_length=255)
    next_of_kin_phone_number = models.CharField(max_length=255)
    doctor_assigned = models.ManyToManyField(Doctor)
    drug_administered = models.ManyToManyField(Drug)
    vital_signs = models.ForeignKey(Vital_signs, null=True, on_delete=models.CASCADE, default='12')


    def __str__(self) -> str:
        return self.first_name



    

