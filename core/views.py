from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("home")


def room(request):
    return HttpResponse("room")
