from django.shortcuts import render


from django.http import HttpResponse, HttpResponseRedirect

from django.contrib import auth

from ..models import *

# Create your views here.


def index(request):
    if request.user.is_authenticated and not request.user.is_anonymous():
        return HttpResponseRedirect("/calendar")
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            log_add("Staff " + user.first_name + " " + user.last_name + " logged in.")
            return HttpResponseRedirect("/calendar")
        else:
            # Show an error page
            return HttpResponseRedirect("/stafflogin")
    else :
        return render(request, 'patients/staffloginPage.html', {})