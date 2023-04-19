from django.shortcuts import render

from django.contrib.auth import authenticate, login

from services.user_module.forms import RegistrationForm


def registration(request):
    form = RegistrationForm()
    return render(request, 'registration.html', context={'form: form'})
