from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello World')
def hello(request):
    return  HttpResponse('Hello Nql')
# Create your views here.
