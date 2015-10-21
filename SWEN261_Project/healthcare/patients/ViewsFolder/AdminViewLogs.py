from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
from datetime import datetime
from datetime import timedelta

# Create your views here.

def index(request):

    user = request.user
    #Redirect if not logged in
    if 'auth.nurse' not in user.get_all_permissions() or 'auth.patient' not in user.get_all_permissions():
        return HttpResponseRedirect("/notauthorized")




    patients = Patient.objects.order_by("firstName")

    visits = HospitalVisit.objects.order_by("dateAdmitted")

    numberInHospitalCurrently = 0

    numberOfPatients = 0

    numberOfVisits = 0

    timeSpentInVisits = 0

    for patient in patients:
        numberOfPatients += 1
        if patient.isAdmitted:
            numberInHospitalCurrently += 1

    for visit in visits:
        if visit.dateDischarged.toordinal() != getOrdinalOfNotYetDischarged():
            numberOfVisits += 1
            timeSpentInVisits += (visit.dateDischarged - visit.dateAdmitted).total_seconds()





    logs = Log.objects.order_by("-dateTime")



    if numberOfVisits == 0:
        context = {"messagenum": get_number_of_unread(user),'logs': logs, "numInHospital": numberInHospitalCurrently,
               "averageVisits": numberOfVisits/numberOfPatients, "averageLengthOfStay": "No visits"}
    else:
        context = {"messagenum": get_number_of_unread(user),'logs': logs, "numInHospital": numberInHospitalCurrently,
               "averageVisits": numberOfVisits/numberOfPatients, "averageLengthOfStay": truncate((timeSpentInVisits / numberOfVisits) / 60 / 60, 3)}
        #averageLengthOfStay is divided twice by 60 to make the number in hours, then passed through truncate to cut it to 3 decimal places.
    return render(request, 'patients/adminViewLogs.html', context)

#Thank David Z from StackOverflow for this function
#We have our team name for a reason.
#http://stackoverflow.com/questions/783897/truncating-floats-in-python
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
