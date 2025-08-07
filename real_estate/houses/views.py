from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import House
from .forms import HouseForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HouseListView(LoginRequiredMixin, ListView):
    model = House
    template_name = "houses/list.html"
    context_object_name = "houses"

class HouseDetailView(LoginRequiredMixin, DetailView):
    model = House
    template_name = "houses/detail.html"
    context_object_name = "house"

class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    form_class = HouseForm
    template_name = "houses/create.html"
    success_url = reverse_lazy('houses:list')
    
    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

class HouseUpdateView(LoginRequiredMixin, UpdateView):
    model = House
    form_class = HouseForm
    template_name = "houses/update.html"
    success_url = reverse_lazy('houses:list')


    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)

class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    template_name = "houses/delete.html"
    success_url = reverse_lazy('houses:list')