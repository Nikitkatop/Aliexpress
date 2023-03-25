from django.shortcuts import render

from django.contrib.auth import authenticate, login


def registration(request):
    print('nice')
    return render(request, 'registration.html')
