# filepath: /home/dreambian/dev/pydev/django-real-estate/real_estate/houses/urls.py
from django.urls import path
from .views import (
    HouseListView, HouseDetailView, HouseCreateView,
    HouseUpdateView, HouseDeleteView, 
)


app_name = 'houses'

urlpatterns = [
    path('', HouseListView.as_view(), name='list'),
    path('<int:pk>/', HouseDetailView.as_view(), name='detail'),
    path('create/', HouseCreateView.as_view(), name='create'),
    path('<int:pk>/update/', HouseUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', HouseDeleteView.as_view(), name='delete'),
]