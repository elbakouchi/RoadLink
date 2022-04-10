from django.urls import path
from .views import GeneratePdf
app_name = 'mission'
urlpatterns = [
    path(r'^pdf/$', GeneratePdf.as_view(), name='generatepdf'),
]