from django.urls import path
from . import views

app_name = 'houses'

urlpatterns = [
    path('', views.house_list, name='list'),            
    path('add/', views.house_create, name='add'),       
    path('<int:pk>/', views.house_detail, name='detail'),
    path('<int:pk>/edit/', views.house_update, name='edit'),
    path('<int:pk>/delete/', views.house_delete, name='delete'),
]
