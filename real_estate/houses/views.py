from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def houses(request):
    return HttpResponse("Hello World!")

def house_list(request):
    return HttpResponse("House List")

def house_create(request):
    return HttpResponse("Create house")

def house_detail(request):
    return HttpResponse("House details")

def house_update(request):
    return HttpResponse("House Update")

def house_delete(request):
    return HttpResponse("House Delete")