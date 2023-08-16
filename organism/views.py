from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Affectation, Organism

# Affectation Views
class AffectationListView(ListView):
    model = Affectation
    template_name = 'affectation/affectation_list.html'
    context_object_name = 'affectations'

class AffectationCreateView(CreateView):
    model = Affectation
    fields = ['name']
    template_name = 'affectation/affectation_form.html'
    success_url = reverse_lazy('organism:affectation_list')

class AffectationUpdateView(UserPassesTestMixin, UpdateView):
    model = Affectation
    fields = ['name']
    template_name = 'affectation/affectation_form.html'
    success_url = reverse_lazy('organism:affectation_list')

    def test_func(self):
        return self.request.user.is_superuser

class AffectationDeleteView(UserPassesTestMixin, DeleteView):
    model = Affectation
    template_name = 'affectation/affectation_confirm_delete.html'
    success_url = reverse_lazy('organism:affectation_list')

    def test_func(self):
        return self.request.user.is_superuser

# Organism Views
class OrganismListView(ListView):
    model = Organism
    template_name = 'organism/organism_list.html'
    context_object_name = 'organisms'

class OrganismCreateView(CreateView):
    model = Organism
    fields = ['ministry', 'province', 'department', 'service', 'telephone', 'fax', 'address', 'description', 'logo']
    template_name = 'organism/organism_form.html'
    success_url = reverse_lazy('organism:organism_list')

class OrganismUpdateView(UserPassesTestMixin, UpdateView):
    model = Organism
    fields = ['ministry', 'province', 'department', 'service', 'telephone', 'fax', 'address', 'description', 'logo']
    template_name = 'organism/organism_form.html'
    success_url = reverse_lazy('organism:organism_list')

    def test_func(self):
        return self.request.user.is_superuser

class OrganismDeleteView(UserPassesTestMixin, DeleteView):
    model = Organism
    template_name = 'organism/organism_confirm_delete.html'
    success_url = reverse_lazy('organism:organism_list')

    def test_func(self):
        return self.request.user.is_superuser
