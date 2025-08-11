from django.views.generic import TemplateView
from houses.models import House

class DashboardView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_houses'] = House.objects.count()
        context['available'] = House.objects.filter(status='available').count()
        context['sold'] = House.objects.filter(status='sold').count()
        context['pending'] = House.objects.filter(status='pending').count()
        context['recent_houses'] = House.objects.order_by('-created_at')[:5]

        return context
