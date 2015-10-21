from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
import datetime

# Create your views here.

def index(request, patientid, reason):

    print("reason " + reason)

    user = request.user
    #Redirect if not logged in
    if 'auth.doctor' not in user.get_all_permissions():
        return HttpResponseRedirect("/notauthorized")

    patientList = Patient.objects.order_by("firstName")

    mainPatient = None

    for patient in patientList:
        if str(patient.id) == patientid:
            mainPatient = patient
            break

    if not mainPatient.isAdmitted:
        newVisit = HospitalVisit(patient=mainPatient, reason=reason, dateAdmitted=datetime.datetime.now(),
                                 dateDischarged=datetime.datetime.fromordinal(getOrdinalOfNotYetDischarged()))
        newVisit.save()
        mainPatient.isAdmitted = True
        mainPatient.save()
        return HttpResponseRedirect("/viewpatient/" + patientid)




    visitList = HospitalVisit.objects.order_by("dateAdmitted")

    patientVisitList = []


    for visit in visitList:
        if mainPatient.id == visit.patient.id:
            patientVisitList += [visit]


    patientVisitList[-1].dateDischarged = datetime.datetime.now()
    patientVisitList[-1].save()

    mainPatient.isAdmitted = False
    mainPatient.save()


    return HttpResponseRedirect("/viewpatient/" + patientid)
