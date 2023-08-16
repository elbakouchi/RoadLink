from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Vehicle
from .forms import VehicleForm


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        form = VehicleForm()
        return render(request, 'vehicle/index.html', {'form': form})
    else:
        return redirect("http://localhost:8000/home/404")


def addVehicle(request):
    if request.POST:
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            success_message = 'Adding done'
            form = VehicleForm()
            return render(request, 'vehicle/index.html', {'form': form, 'success': success_message})
    else:
        if request.user.is_authenticated:
            form = VehicleForm()
            error_message = 'Something went wrong error'
            return render(request, 'vehicle/index.html', {'form': form, 'error': error_message})


def showVehicles(request):
    if request.method == 'POST' and 'searchb' in request.POST:
        search_query = request.POST.get('search_box')
        vehiclesList = Vehicle.objects.filter(registration_plate=search_query)
        return render(request, 'vehicle/vehiclelist.html', {'vehiclesList': vehiclesList})
    elif request.method == 'POST' and 'viewallb' in request.POST:
        vehiclesList = Vehicle.objects.all()
        return render(request, 'vehicle/vehiclelist.html', {'vehiclesList': vehiclesList})
    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                vehiclesList = Vehicle.objects.all()
            else:
                vehiclesList = Vehicle.objects.filter(owner=request.user)
            return render(request, 'vehicle/vehiclelist.html', {'vehiclesList': vehiclesList})
        else:
            return redirect("http://localhost:8000/home/404")


def delete(request, id):
    if request.POST:
        # form=RepairForm(request.POST)
        # if form.is_valid():
        #     instance=form.save(commit=False)
        #     instance.registeredUser=request.user
        #     instance.save()
        #     success_message='Issue Registered'
        #     form=RepairForm()
        return render(request, 'vehicle/index.html', {'form': form, 'user': request.user})
    else:
        if request.user.is_authenticated:
            vehicle = Vehicle.objects.get(id=id)
            vehicle.delete()
            return redirect('http://localhost:8000/vehicle/vehicles')
        else:
            return redirect("http://localhost:8000/home/404")


def edit(request, id):
    if request.method == "POST":
        vehicle = Vehicle.objects.get(id=id)
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('http://localhost:8000/vehicle/vehicles')
    elif request.user.is_authenticated:
        vehicle = Vehicle.objects.get(id=id)
        form = VehicleForm(instance=vehicle)
        return render(request, 'vehicle/vehicleEdit.html', {'form': form, 'id': id})
    

from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Parking, Vehicle

class ParkingListView(ListView):
    model = Parking
    template_name = 'vehicle/parking_list.html'
    context_object_name = 'parkings'

class ParkingCreateView(CreateView):
    model = Parking
    fields = ['name']
    template_name = 'vehicle/parking_form.html'
    success_url = reverse_lazy('vehicle:parking_list')

class ParkingUpdateView(UserPassesTestMixin, UpdateView):
    model = Parking
    fields = ['name']
    template_name = 'vehicle/parking_form.html'
    success_url = reverse_lazy('vehicle:parking_list')

    def test_func(self):
        return self.request.user.is_superuser

class ParkingDeleteView(UserPassesTestMixin, DeleteView):
    model = Parking
    template_name = 'vehicle/parking_confirm_delete.html'
    success_url = reverse_lazy('vehicle:parking_list')

    def test_func(self):
        return self.request.user.is_superuser

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle/vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['brand', 'model', 'registration_plate', 'parking', 'vehicle_status', 'insurance_status', 'fuel_type', 'mileage', 'vehicle_type', 'image']
    template_name = 'vehicle/vehicle_form.html'
    success_url = reverse_lazy('vehicle:vehicle_list')

class VehicleUpdateView(UserPassesTestMixin, UpdateView):
    model = Vehicle
    fields = ['brand', 'model', 'registration_plate', 'parking', 'vehicle_status', 'insurance_status', 'fuel_type', 'mileage', 'vehicle_type', 'image']
    template_name = 'vehicle/vehicle_form.html'
    success_url = reverse_lazy('vehicle:vehicle_list')

    def test_func(self):
        return self.request.user.is_superuser

class VehicleDeleteView(UserPassesTestMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle:vehicle_list')

    def test_func(self):
        return self.request.user.is_superuser

