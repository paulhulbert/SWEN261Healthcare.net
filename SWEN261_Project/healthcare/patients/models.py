#IF YOU ARE NOT ARI YOU SHOULD NOT TOUCH THIS FILE!
#Copyright StackOverflowGooglers 2015

from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

states = [
        'Alabama',
        'Alaska',
        'American Samoa',
        'Arkansas',
        'Arizona',
        'California',
        'Colorado',
        'Connecticut',
        'Delaware',
        'District of Columbia',
        'Florida',
        'Georgia',
        'Guam',
        'Hawaii',
        'Idaho',
        'Illinois',
        'Indiana',
        'Iowa',
        'Kansas',
        'Kentucky',
        'Louisiana',
        'Maine',
        'Maryland',
        'Massachusetts',
        'Michigan',
        'Minnesota',
        'Mississippi',
        'Missouri',
        'Montana',
        'Nebraska',
        'Nevada',
        'New Hampshire',
        'New Jersey',
        'New Mexico',
        'New York',
        'North Carolina',
        'North Dakota',
        'Northern Mariana Islands',
        'Ohio',
        'Oklahoma',
        'Oregon',
        'Pennsylvania',
        'Puerto Rico',
        'Rhode Island',
        'South Carolina',
        'South Dakota',
        'Tennessee',
        'Texas',
        'Utah',
        'Vermont',
        'Virginia',
        'Virgin Islands',
        'Washington',
        'West Virginia',
        'Wisconsin',
        'Wyoming'
]

def log_add(task):
    entry = Log(action=task)
    entry.save()


def get_number_of_unread(person):
    allMessages = PrivateMessage.objects.order_by("dateTime")

    numberUnread = 0

    for message in allMessages:
        if message.receiver == person and message.isUnread == True:
            numberUnread += 1

    return numberUnread

# Create your models here.
class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    action = models.CharField(max_length=1000)
    dateTime = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.action

class Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userNameField = models.CharField(max_length=1000)
    firstName = models.CharField(max_length=1000)
    lastName = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)

    def __str__(self):
        return self.firstName + " " + self.lastName


class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userNameField = models.CharField(max_length=1000)
    firstName = models.CharField(max_length=1000)
    lastName = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = models.CharField(max_length=1000)
    address1 = models.CharField(max_length=1000)
    address2 = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    insuranceName = models.CharField(max_length=1000)
    insuranceID = models.CharField(max_length=1000)
    hospital = models.ForeignKey(Hospital)
    emergencyContactFirstName = models.CharField(max_length=1000)
    emergencyContactLastName = models.CharField(max_length=1000)
    emergencyContactPhone = models.CharField(max_length=1000)
    emergencyContactEmail = models.CharField(max_length=1000)
    medicalInformation = models.CharField(max_length=1000)
    isAdmitted = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName + " " +  self.lastName



class Nurse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userNameField = models.CharField(max_length=1000)
    firstName = models.CharField(max_length=1000)
    lastName = models.CharField(max_length=1000)
    phone = models.CharField(max_length=1000)
    hospital = models.ForeignKey(Hospital)

    def __str__(self):
        return self.firstName + " " + self.lastName

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    dateTime = models.DateTimeField()
    hospital = models.ForeignKey(Hospital)

    def __str__(self):
        return "Appointment"#Not sure what to return




class PrivateMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User)
    dateTime = models.DateTimeField()
    message = models.CharField(max_length=1000)
    isUnread = models.BooleanField(default=True)


    def __str__(self):
        return "At " + str(self.dateTime) + ", " + str(self.sender) + " sent: " + str(self.message) + "---" + str(self.isUnread)


class HospitalVisit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient)
    reason = models.CharField(max_length=1000)
    dateAdmitted = models.DateTimeField()
    dateDischarged = models.DateTimeField()  #Ordinal of a discharge that has not happened yet is: 735000

def getOrdinalOfNotYetDischarged():
    return 735000