from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def madhan (request):
    return HttpResponse('<marquee><h1>Madhan is a Selfish</h1></marquee>')

def harsha (request):
    return HttpResponse('<marquee><h1><i>Harsha is a cool Hearted Persons</i></h1></marquee>')

def mahesh (request):
    return HttpResponse('<marquee><h1><i>Mahesh is a Gold Hearted Person</marquee></h1></i>')