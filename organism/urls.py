from django.urls import path
from .views import (
    AffectationListView, AffectationCreateView, AffectationUpdateView, AffectationDeleteView,
    OrganismListView, OrganismCreateView, OrganismUpdateView, OrganismDeleteView,
)

app_name = 'organism'  # Replace with your app name

urlpatterns = [
    # Other URLs...

    # Affectation URLs
    path('affectations/', AffectationListView.as_view(), name='affectation_list'),
    path('affectations/create/', AffectationCreateView.as_view(), name='affectation_create'),
    path('affectations/<int:pk>/update/', AffectationUpdateView.as_view(), name='affectation_update'),
    path('affectations/<int:pk>/delete/', AffectationDeleteView.as_view(), name='affectation_delete'),

    # Organism URLs
    path('organisms/', OrganismListView.as_view(), name='organism_list'),
    path('organisms/create/', OrganismCreateView.as_view(), name='organism_create'),
    path('organisms/<int:pk>/update/', OrganismUpdateView.as_view(), name='organism_update'),
    path('organisms/<int:pk>/delete/', OrganismDeleteView.as_view(), name='organism_delete'),
]
