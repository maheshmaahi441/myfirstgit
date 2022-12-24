from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dharshan (request):
    return HttpResponse('<marquee><h1><i>Mr Atittude</i></h1></marquee>')

def manohar (request):
    return HttpResponse('<marquee><h1><i>Money Minded</marquee></h1></i>')
