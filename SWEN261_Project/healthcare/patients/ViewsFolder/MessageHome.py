from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect
from ..models import *

from django.contrib.auth.models import User

# Create your views here.

def index(request):

    user = request.user
    #Redirect if not logged in
    if user.is_anonymous():
        return HttpResponseRedirect("/notauthorized")


    userList = User.objects.order_by("first_name")

    users = []

    allMessages = PrivateMessage.objects.filter(receiver=user).order_by("dateTime")

    for user1 in userList:
        if user1 == user:
            name = user1.first_name + " " + user1.last_name
            continue
        userURL = "/messaging/" + str(user1.username)
        unread = 0
        for message in allMessages:
            if message.sender == user1 and message.isUnread == True:
                unread += 1

        users += [(user1.first_name + " " + user1.last_name, userURL, unread)]



    permissions = user.get_all_permissions()
    pOd = 'patient' if 'auth.patient' in permissions else 'doctor' if 'auth.doctor' in permissions else 'nurse'

    context = {"messagenum": get_number_of_unread(user), "name": name, "pOd": pOd, "people": users}
    return render(request, 'patients/messageHome.html', context)
