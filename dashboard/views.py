from django.views.generic import TemplateView
from houses.models import House
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_houses = House.objects.filter(agent=user)
        
        context['total_houses'] = user_houses.count()
        context['available'] = user_houses.filter(status='available').count()
        context['sold'] = user_houses.filter(status='sold').count()
        context['pending'] = user_houses.filter(status='pending').count()
        context['recent_houses'] = user_houses.order_by('-created_at')[:5]

        return context
