#Copyright 2015 StackOverflowGooglers

from django.shortcuts import render
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404


from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    #user = get_object_or_404(User, pk=user_id)
    testString = "Hello world from HomePage.py"
    context = {'testString': testString}
    return render(request, 'patients/index.html', context)


#Copyright 2015 StackOverflowGooglers