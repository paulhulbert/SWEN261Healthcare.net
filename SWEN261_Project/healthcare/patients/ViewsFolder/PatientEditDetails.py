from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from ..models import *
from datetime import datetime

from django.contrib import auth
# Create your views here.
def index(request):
    user = request.user
    testString = 'auth.patient' in user.get_all_permissions()

    if not testString:
        return HttpResponseRedirect("/notauthorized")
    if request.method == "POST":

        patient = Patient.objects.get(userNameField=request.user.username)

        context = {"messagenum": get_number_of_unread(user),'firstName': patient.firstName, 'lastName': patient.lastName, 'email': patient.email,
               'city': patient.city, 'state': patient.state, 'address1': patient.address1,
               'phone': patient.phone, 'insuranceName': patient.insuranceName, 'insuranceID': patient.insuranceID,
               'hospital': patient.hospital,
               'emergencyContactFirstName': patient.emergencyContactFirstName,
               'emergencyContactLastName': patient.emergencyContactLastName,
               'emergencyContactPhone': patient.emergencyContactPhone,
               'emergencyContactEmail': patient.emergencyContactEmail,
               'medicalInformation': patient.medicalInformation,
                   'states' : states,
                   'errortext' : "Missing Required Field",
                   "hospitals" : Hospital.objects.order_by("name")}



        firstName = request.POST.get('firstname', '')
        lastName = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        address1 = request.POST.get('address1', '')
        phone = request.POST.get('phone', '')
        insuranceName = request.POST.get('insurancename', '')
        insuranceID = request.POST.get('insuranceid', '')
        hospital = request.POST.get('hospital', '')
        emergencyContactFirstName = request.POST.get('emergencycontactfirstname', '')
        emergencyContactLastName = request.POST.get('emergencycontactlastname', '')
        emergencyContactPhone = request.POST.get('emergencycontactphone', '')
        emergencyContactEmail = request.POST.get('emergencycontactemail', '')
        medicalInformation = request.POST.get('medicalinformation', '')
        password = request.POST.get('password', '')
        confirmPassword = request.POST.get('confirmpassword', '')


        if firstName == '' or lastName == '' or email == '' or city == '' or state == '' or address1 == '' or phone == '' or \
            insuranceName == '' or insuranceID == '' or hospital == '' or emergencyContactFirstName == '' \
                or emergencyContactLastName == '' or emergencyContactPhone == '' \
                or emergencyContactEmail == ''\
                or medicalInformation == '':
            return render(request, 'patients/patientEditPatientDetails.html', context)


        patient.firstName = firstName
        patient.lastName = lastName
        patient.email = email
        patient.city = city
        patient.state = state
        patient.address1 = address1
        patient.phone = phone
        patient.insuranceName = insuranceName
        patient.insuranceID = insuranceID
        patient.hospital = Hospital.objects.get(name=hospital)
        patient.emergencyContactFirstName = emergencyContactFirstName
        patient.emergencyContactLastName = emergencyContactLastName
        patient.emergencyContactPhone = emergencyContactPhone
        patient.emergencyContactEmail = emergencyContactEmail
        patient.medicalInformation = medicalInformation

        user.firstName = firstName
        user.lastName = lastName
        user.set_password(password)

        patient.save()
        user.save()

        user = auth.authenticate(username=user.username, password=password)
        auth.login(request, user)

        log_add("Patient " + str(patient) + " edited details.")

        return HttpResponseRedirect("/patientviewpatientdetails")

    else :

        patient = Patient.objects.get(userNameField=request.user.username)

        context = {"messagenum": get_number_of_unread(user),'firstName': patient.firstName, 'lastName': patient.lastName, 'email': patient.email,
               'city': patient.city, 'state': patient.state, 'address1': patient.address1,
               'phone': patient.phone, 'insuranceName': patient.insuranceName, 'insuranceID': patient.insuranceID,
               'hospital': patient.hospital,
               'emergencyContactFirstName': patient.emergencyContactFirstName,
               'emergencyContactLastName': patient.emergencyContactLastName,
               'emergencyContactPhone': patient.emergencyContactPhone,
               'emergencyContactEmail': patient.emergencyContactEmail,
               'medicalInformation': patient.medicalInformation, 'states' : states,
                   "hospitals" : Hospital.objects.order_by("name")}


        return render(request, 'patients/patientEditPatientDetails.html', context)
