"""
================R_O_U_T_E_R==============

"""
from django.contrib import admin
from django.urls import path, include
from tours import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),
    path('departure/<str:departure>', views.DepartureView, name='departure'),
    path('tour/<int:id>', views.TourView, name='tour')
]
