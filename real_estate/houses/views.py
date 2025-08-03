from django.shortcuts import render, get_object_or_404, redirect
from .models import House
from .forms import HouseForm

def house_list(request):
    houses = House.objects.all()
    return render(request, "houses/list.html", {'houses': houses})

def house_create(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('houses:list')
    else:
        form = HouseForm()
    return render(request, "houses/create.html", {'form': form})

def house_detail(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, "houses/detail.html", {'house': house})

def house_update(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('houses:detail', pk=pk)
    else:
        form = HouseForm(instance=house)
    return render(request, "houses/update.html", {'form': form})

def house_delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        house.delete()
        return redirect('houses:list')
    return render(request, "houses/delete.html", {'house': house})
