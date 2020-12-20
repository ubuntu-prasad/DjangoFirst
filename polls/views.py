from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def appDetails(request):
    return HttpResponse("This is Poll app developed by Prasad for learnign Django python framework.")