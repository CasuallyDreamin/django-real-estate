from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import House
from .forms import HouseForm

class HouseListView(ListView):
    model = House
    template_name = "houses/list.html"
    context_object_name = "houses"

class HouseDetailView(DetailView):
    model = House
    template_name = "houses/detail.html"
    context_object_name = "house"

class HouseCreateView(CreateView):
    model = House
    form_class = HouseForm
    template_name = "houses/create.html"
    success_url = reverse_lazy('houses:list')

class HouseUpdateView(UpdateView):
    model = House
    form_class = HouseForm
    template_name = "houses/update.html"
    success_url = reverse_lazy('houses:list')

class HouseDeleteView(DeleteView):
    model = House
    template_name = "houses/delete.html"
    success_url = reverse_lazy('houses:list')