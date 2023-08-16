from django.urls import path
from . import views
app_name='home'
urlpatterns = [
	path('404', views.notfound,name='index'),
    path('', views.HomePage.as_view(),name='index'),
]