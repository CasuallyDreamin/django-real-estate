from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('houses/', include('houses.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', RedirectView.as_view(url="/dashboard/"))

]
