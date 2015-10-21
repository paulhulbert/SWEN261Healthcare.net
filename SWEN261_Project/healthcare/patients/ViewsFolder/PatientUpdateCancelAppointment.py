from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
from datetime import datetime

# Create your views here.
def index(request, text):
    user = request.user
    testString = 'auth.patient' in user.get_all_permissions()
    
    if not testString:
        return HttpResponseRedirect("/notauthorized")

    patient=Patient.objects.get(userNameField=user.username)
    appointment = Appointment.objects.get(id=text)
    
    if request.method == "POST":
        month = request.POST.get('month', '')
        day = request.POST.get('day', '')
        year = request.POST.get('year', '')
        doctor = request.POST.get('doctor', '')
        time = request.POST.get('time', '')
        
        if month == '' or day == '' or year == '' or doctor == '' or time == '':
            return render(request, 'patients/patientUpdateCancelAppointment.html',
                          {"messagenum": get_number_of_unread(user),"name": patient.firstName + " " + patient.lastName, "errortext" : "Missing Required Field", "doctors" : Doctor.objects.order_by("firstName"),
                                                                                "cancellink" : "/patientdeleteappointment/" + text})


        appointment.doctor = Doctor.objects.get(lastName=doctor.split()[1])
        appointment.dateTime = datetime.strptime(month + ' ' + day +  ' ' + year + ' ' + time + "00", '%m %d %Y %H:%M%S')

        appointment.save()

        log_add("Patient " + str(patient) + " updated an appointment.")

        return HttpResponseRedirect("/calendar")

    else :
        return render(request, 'patients/patientUpdateCancelAppointment.html', {"messagenum": get_number_of_unread(user),"name": patient.firstName + " " + patient.lastName,
                                                                                "doctors" : Doctor.objects.order_by("firstName"),
                                                                                "appointment": appointment,
                                                                                "cancellink" : "/patientdeleteappointment/" + text})


def cancelAppointment(request, text):
    appointment = Appointment.objects.get(id=text)
    appointment.delete()

    patient=Patient.objects.get(userNameField=request.user.username)
    log_add("Patient " + str(patient) + " cancelled an appointment.")

    return HttpResponseRedirect("/calendar")
