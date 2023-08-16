from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Budget

class BudgetListView(ListView):
    model = Budget
    template_name = 'budget/budget_list.html'
    context_object_name = 'budgets'

class BudgetCreateView(CreateView):
    model = Budget
    fields = ['title', 'fiscal_year_start', 'fiscal_year_end', 'amount', 'balance']
    template_name = 'budget/budget_form.html'
    success_url = reverse_lazy('budget:budget_list')

class BudgetUpdateView(UserPassesTestMixin, UpdateView):
    model = Budget
    fields = ['title', 'fiscal_year_start', 'fiscal_year_end', 'amount', 'balance']
    template_name = 'budget/budget_form.html'
    success_url = reverse_lazy('budget:budget_list')

    def test_func(self):
        return self.request.user.is_superuser

class BudgetDeleteView(UserPassesTestMixin, DeleteView):
    model = Budget
    template_name = 'budget/budget_confirm_delete.html'
    success_url = reverse_lazy('budget:budget_list')

    def test_func(self):
        return self.request.user.is_superuser

