from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^administration/$', views.AdminHome, name='administration'),
    url(r'^viewlogs/$', views.ViewLogs, name='ViewLogs'),
    url(r'^createdoctor/$', views.CreateDoctor, name='CreateDoctor'),
    url(r'^createnurse/$', views.CreateNurse, name='CreateNurse'),
    url(r'^calendar/(?P<cal_year>[0-9]{4})/(?P<cal_month>[0-9]+)/(?P<cal_day>[0-9]+)/$', views.PatientDoctorCalendar, name='PatientDoctorCalendar'),
    url(r'^calendar/(?P<cal_year>[0-9]{4})/(?P<cal_month>[0-9]+)/$', views.PatientDoctorCalendar, name='PatientDoctorCalendar'),
    url(r'^calendar/(?P<cal_year>[0-9]{4})/$', views.PatientDoctorCalendar, name='PatientDoctorCalendar'),
    url(r'^listofpatients/$', views.ListOfPatients, name='ListOfPatients'),
    url(r'^viewpatient/(?P<text>[a-z A-Z 0-9 -]+)/$', views.DoctorViewPatientDetails, name='DoctorViewPatientDetails'),
    url(r'^messaging/$', views.MessageHome, name='MessageHome'),
    url(r'^messaging/(?P<text>[a-z A-Z 0-9 - _]+)/$', views.MessageSend, name='MessageSend'),
    url(r'^nursecalendar/$', views.NurseHome, name='NurseHome'),
    url(r'^nursecalendar/(?P<patientdoctorid>[a-z A-Z 0-9 -]+)/$', views.NurseWeek, name='NurseWeek'),
    url(r'^nursecalendar/(?P<patientdoctorid>[a-z A-Z 0-9 -]+)/(?P<daynumber>[0-6]{1})/$', views.NurseDay, name='NurseDay'),
    url(r'^calendar/', views.PatientDoctorCalendar, name='PatientDoctorCalendar'),
    url(r'^logout/', views.PatientDoctorNurseLogout, name='PatientDoctorNurseLogout'),
    url(r'^login/$', views.PatientDoctorNurseLogin, name='PatientDoctorNurseLogin'),
    url(r'^stafflogin/$', views.DoctorNurseLogin, name='DoctorNurseLogin'),
    url(r'^patientregistration/$', views.PatientRegister, name='PatientRegister'),
    url(r'^patientviewpatientdetails/$', views.PatientViewPatientDetails, name='PatientViewPatientDetails'),
    url(r'^patienteditpatientdetails/$', views.PatientEditPatientDetails, name='PatientEditPatientDetails'),
    url(r'^notauthorized/$', views.NotAuthorized, name='NotAuthorized'),
    url(r'^patientcreateappointment/$', views.PatientCreateAppointment, name='PatientCreateAppointment'),
    url(r'^doctorcreateappointment/$', views.DoctorCreateAppointment, name='DoctorCreateAppointment'),
    url(r'^patientupdatecancelappointment/(?P<text>[a-z A-Z 0-9 -]+)/$',
        views.PatientUpdateCancelAppointment, name='PatientUpdateCancelAppointment'),
    url(r'^nurseupdateappointment/(?P<text>[a-z A-Z 0-9 -]+)/$',
        views.NurseUpdateAppointment, name='NurseUpdateAppointment'),
    url(r'^doctorupdatecancelappointment/(?P<text>[a-z A-Z 0-9 -]+)/$',
        views.DoctorUpdateCancelAppointment, name='DoctorUpdateCancelAppointment'),
    url(r'^patientdeleteappointment/(?P<text>[a-z A-Z 0-9 -]+)/$',
        views.PatientDeleteAppointment, name='PatientDeleteAppointment'),
    url(r'^doctordeleteappointment/(?P<text>[a-z A-Z 0-9 -]+)/$',
        views.DoctorDeleteAppointment, name='DoctorDeleteAppointment'),
]

#Copyright StackOverflowGooglers 2015
