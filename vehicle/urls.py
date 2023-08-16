from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='vehicle'
urlpatterns = [
    path('', views.index,name='index'),
    path('addVehicle',views.addVehicle,name='addVehicle'),
    path('vehicles',views.showVehicles,name='showVehicles'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from .views import (
    ParkingListView, ParkingCreateView, ParkingUpdateView, ParkingDeleteView,
    VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView,
)


urlpatterns += [
    # Parking URLs
    path('parkings/', ParkingListView.as_view(), name='parking_list'),
    path('parkings/create/', ParkingCreateView.as_view(), name='parking_create'),
    path('parkings/<int:pk>/update/', ParkingUpdateView.as_view(), name='parking_update'),
    path('parkings/<int:pk>/delete/', ParkingDeleteView.as_view(), name='parking_delete'),

    # Vehicle URLs
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicles/<int:pk>/update/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),
]
