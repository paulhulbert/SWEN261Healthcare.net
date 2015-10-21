from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
from datetime import datetime

# Create your views here.
def index(request, text):
    user = request.user
    testString = 'auth.nurse' in user.get_all_permissions()

    userobj = Nurse.objects.get(userNameField=user.username)

    appointment = Appointment.objects.get(id=text)

    patient = appointment.patient
    doctor = appointment.doctor

    if not testString:
        return HttpResponseRedirect("/notauthorized")
    if request.method == "POST":
        month = request.POST.get('month', '')
        day = request.POST.get('day', '')
        year = request.POST.get('year', '')
        time = request.POST.get('time', '')
        if month == '' or day == '' or year == '' or patient == '' or time == '':
            return render(request, 'patients/nurseUpdateAppointment.html',
                          {"messagenum": get_number_of_unread(user),"errortext" : "Missing Required Field", 'patient': patient, 'doctor': doctor})








        appointment.dateTime = datetime.strptime(month + ' ' + day +  ' ' + year + ' ' + time + "00", '%B %d %Y %H:%M%S')




        appointment.save()

        log_add("Nurse " + user.first_name + " " + user.last_name + " edited an appointment.")

        return HttpResponseRedirect("/nursecalendar")

    else :



        return render(request, 'patients/nurseUpdateAppointment.html', {"name": userobj.firstName + " " + userobj.lastName, "messagenum": get_number_of_unread(user),'patient': patient, 'doctor': doctor})
