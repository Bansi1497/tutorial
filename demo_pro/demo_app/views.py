from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def mess(request):
    return HttpResponse('<h2> Welcome To Django !!!!!!</h2>')
