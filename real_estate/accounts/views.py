from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration succesful! you are now logged in.")
            return redirect('houses:list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})