from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    user = request.user
    userobj = Doctor.objects.get(userNameField=user.username)
    testString = 'auth.doctor' in user.get_all_permissions()

    if not testString:
        return HttpResponseRedirect("/notauthorized")
    if request.method == "POST":
        month = request.POST.get('month', '')
        day = request.POST.get('day', '')
        year = request.POST.get('year', '')
        patient = request.POST.get('patient', '')
        time = request.POST.get('time', '')
        if month == '' or day == '' or year == '' or patient == '' or time == '':
            return render(request, 'patients/doctorCreateAppointment.html',
                          {"name": userobj.firstName + " " + userobj.lastName, "messagenum": get_number_of_unread(user),"errortext" : "Missing Required Field", "patients" : Patient.objects.order_by("firstName")})


        doctor=Doctor.objects.get(userNameField=user.username)
        patient = Patient.objects.get(lastName=patient.split()[1])


        try:
            appointment = Appointment(doctor=doctor, patient=patient,
                                  dateTime=datetime.strptime(month + ' ' + day + ' ' + year + ' ' + time + "00", '%B %d %Y %H:%M%S'),
                                  hospital=patient.hospital)
        except ValueError:
            return render(request, 'patients/doctorCreateAppointment.html',
                          {"name": userobj.firstName + " " + userobj.lastName, "messagenum": get_number_of_unread(user),"errortext" : "Invalid Day", "patients" : Patient.objects.order_by("firstName")})


        timeAdjustment = appointment.dateTime
        timeAdjustment -= timedelta(hours=4)

        appointment.dateTime = timeAdjustment

        appointment.save()

        log_add("Doctor " + str(doctor) + " created an appointment.")

        return HttpResponseRedirect("/calendar")

    else :


        return render(request, 'patients/doctorCreateAppointment.html', {"name": userobj.firstName + " " + userobj.lastName, "messagenum": get_number_of_unread(user),"patients" : Patient.objects.order_by("firstName") })
