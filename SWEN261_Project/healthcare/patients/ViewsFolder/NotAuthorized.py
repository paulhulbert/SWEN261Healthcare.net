#Copyright StackOverflowGooglers 2015
from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib import auth
from django.contrib.contenttypes.models import ContentType

# Create your views here.


def index(request):

    return render(request, 'patients/notAuthorized.html', {})

#Copyright StackOverflowGooglers 2015
