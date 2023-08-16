from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import District

class DistrictListView(ListView):
    model = District
    template_name = 'division/district_list.html'
    context_object_name = 'districts'

class DistrictCreateView(CreateView):
    model = District
    fields = ['name']
    template_name = 'division/district_form.html'
    success_url = reverse_lazy('division:district_list')

class DistrictUpdateView(UserPassesTestMixin, UpdateView):
    model = District
    fields = ['name']
    template_name = 'division/district_form.html'
    success_url = reverse_lazy('division:district_list')

    def test_func(self):
        return self.request.user.is_superuser

class DistrictDeleteView(UserPassesTestMixin, DeleteView):
    model = District
    template_name = 'division/district_confirm_delete.html'
    success_url = reverse_lazy('division:district_list')

    def test_func(self):
        return self.request.user.is_superuser
