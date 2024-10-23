from django.shortcuts import render
from django.http import HttpResponse

def hello_world_http(request):
    return HttpResponse("hello world")
