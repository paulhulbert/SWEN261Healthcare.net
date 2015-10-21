import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings')

import django
django.setup()

from patients.models import Hospital, Patient,Doctor,Nurse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

def populate():
    hosp = Hospital(name = 'Test Hospital')
    hosp.save()

    user_content = ContentType.objects.get_for_model(User)
    patientPerm = Permission.objects.create(codename='patient',\
                                            name='Is Patient',\
                                            content_type=user_content)
    doctorPerm = Permission.objects.create(codename='doctor',\
                                           name='Is Doctor',\
                                           content_type=user_content)

    nursePerm = Permission.objects.create(codename='nurse',\
                                          name='Is Nurse',\
                                          content_type=user_content)        
    patientPerm.save()
    doctorPerm.save()
    nursePerm.save()
        
    
    u1 = User.objects.create_user(username='test_patient',\
                                  email='test_patient@rit.edu',\
                                  password = 'pass')
    u1.first_name = 'Test'
    u1.last_name = 'Patient'
    u1.user_permissions.add(patientPerm)
    u1.save()
    u2 = User.objects.create_user(username='test_doctor',\
                                  email='test_doctor@rit.edu',\
                                  password = 'pass')
    u2.first_name = 'Test'
    u2.last_name = 'Doctor'
    u2.user_permissions.add(doctorPerm)
    u2.save()
    u3 = User.objects.create_user(username='test_nurse',\
                                  email='test_nurse@rit.edu',\
                                  password = 'pass')
    u3.first_name = 'Test'
    u3.last_name = 'Nurse'
    u3.user_permissions.add(nursePerm)
    u3.save()
    p1 = Patient(firstName= 'Test',\
                 lastName= 'Patient', \
                 hospital=hosp, \
                 userNameField='test_patient', \
                 email='test_patient@rit.edu', \
                 city='Rochester', \
                 state='New York', \
                 address1='test road.', \
                 phone='(888) 888-8888', \
                 insuranceID= '001', \
                 insuranceName='testcare', \
                 emergencyContactEmail='sburtner@rit.edu', \
                 emergencyContactFirstName='Stuart', \
                 emergencyContactLastName='Burtner', \
                 emergencyContactPhone='(555) 555-5555', \
                 medicalInformation='nothing')

    p1.save()
    doc = Doctor(userNameField= 'test_doctor',\
                 firstName= 'Test',\
                 lastName= 'Doctor',\
                 phone= '(555) 555-5555')

    doc.save()
    nur = Nurse(userNameField = 'test_nurse',\
                firstName = 'Test',\
                lastName = 'Nurse',\
                phone = '(555) 555-5555',\
                hospital = hosp)
    nur.save()

populate()
print('Initialization complete')
input("Press enter to continue")
