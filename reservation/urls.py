from django.urls import path
from reservation import views

urlpatterns = [
    path('building/<int:building_no>/<int:classroom_no>/reservation/', views.reservation, name='reservation'),
    path('book-manage/', views.book_manage, name='book_manage'),
    path('manager-page/', views.manager, name='manager_page'),
    path('reservation-confirm/<int:reservation_id>', views.reservation_confirm, name='reservation_confirm'),
    path('reservation-detail/<int:pk>', views.reservationDetail.as_view(), name='detail'),
]
