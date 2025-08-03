from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def house_list(request):
    return render(request, "houses/list.html")

def house_create(request):
    return render(request, "houses/create.html")

def house_detail(request):
    return render(request, "houses/detail.html")

def house_update(request):
    return render(request, "houses/update.html")

def house_delete(request):
    return render(request, "houses/delete.html")