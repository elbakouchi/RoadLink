from django.urls import path
from . import views

app_name = 'booking'
urlpatterns = [
    path('', views.index, name='index'),
    # path('book',views.book,name='book'),
    # path('bookings',views.booking,name='bookings'),
    path('pay', views.pay, name='pay'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('changestatus/<int:id>', views.change, name='delete'),

]

from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns += [
    path('bookings/', BookListView.as_view(), name='booking_list'),
    path('bookings/create/', BookCreateView.as_view(), name='booking_create'),
    path('bookings/<int:pk>/update/', BookUpdateView.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', BookDeleteView.as_view(), name='booking_delete'),
]
