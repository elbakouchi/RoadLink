from django.urls import path
from .views import DistrictListView, DistrictCreateView, DistrictUpdateView, DistrictDeleteView

app_name = 'division'

urlpatterns = [
    path('districts/', DistrictListView.as_view(), name='district_list'),
    path('districts/create/', DistrictCreateView.as_view(), name='district_create'),
    path('districts/<int:pk>/update/', DistrictUpdateView.as_view(), name='district_update'),
    path('districts/<int:pk>/delete/', DistrictDeleteView.as_view(), name='district_delete'),
]
