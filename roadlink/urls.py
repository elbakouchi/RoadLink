"""roadlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Le Parc Tahnouate'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('divisions/', include('district.urls')),
    path('bookings/', include('booking.urls')),
    path('budgets/', include('budget.urls')),
    # path('driver/', include('driver.urls')),
    path('mission/', include('mission.urls')),
    path('organism/', include('organism.urls')),
    # path('repair/', include('repair.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('', include('home.urls')),
    # path('report/', include('report.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
