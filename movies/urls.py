from django.urls import path
from . import views
from movies.admin import custom_admin_site
from django.contrib import admin

urlpatterns = [

    # Home Page / Movie List
    path('', views.movie_list, name='movie_list'),

    # Movie Detail Page
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # Seat Reservation
    path('reserve/<int:seat_id>/', views.reserve_seat, name='reserve_seat'),

    # Payment Page
    path('payment/<int:seat_id>/', views.payment_page, name='payment_page'),

    # Payment Failed
    path('payment-failed/<int:seat_id>/', views.payment_failed, name='payment_failed'),

    # Confirm Booking
    path('confirm/<int:seat_id>/', views.confirm_booking, name='confirm_booking'),

    # Admin Dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Success page
    path('success/', views.success, name='success'),



path('admin/', admin.site.urls),
]