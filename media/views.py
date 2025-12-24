from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def media(request):
    return HttpResponse("Hello from media")