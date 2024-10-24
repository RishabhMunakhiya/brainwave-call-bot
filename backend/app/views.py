from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Patient, Appointment

def get_appointments(request):
    appointments = Appointment.objects.all().values()
    return JsonResponse(list(appointments), safe=False)

def book_appointment(request):
    if request.method == "POST":
        data = request.POST
        patient = Patient.objects.create(
            name=data['name'],
            phone=data['phone'],
            symptoms=data['symptoms']
        )
        Appointment.objects.create(
            patient=patient,
            date=data['date'],
            doctor=data['doctor']
        )
        return JsonResponse({"status": "Appointment booked"})
