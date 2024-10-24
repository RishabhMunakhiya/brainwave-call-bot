from datetime import datetime, timedelta
from .models import Appointment

def get_available_slots():
    today = datetime.today()
    next_week = today + timedelta(days=7)
    return Appointment.objects.filter(date__range=[today, next_week])
