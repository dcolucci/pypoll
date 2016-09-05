# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world.  You're at the polls index")

def show(request):
    return HttpResponse("Here is a different route")
