from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    symptoms = models.TextField()
    urgency = models.BooleanField(default=False)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=100)