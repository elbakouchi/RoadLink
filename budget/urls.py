from django.urls import path
from .views import (
    BudgetListView, BudgetCreateView, BudgetUpdateView, BudgetDeleteView,
)

app_name = 'budget'  # Replace with your app name

urlpatterns = [
    # Other URLs...

    # Budget URLs
    path('budgets/', BudgetListView.as_view(), name='budget_list'),
    path('budgets/create/', BudgetCreateView.as_view(), name='budget_create'),
    path('budgets/<int:pk>/update/', BudgetUpdateView.as_view(), name='budget_update'),
    path('budgets/<int:pk>/delete/', BudgetDeleteView.as_view(), name='budget_delete'),
]
