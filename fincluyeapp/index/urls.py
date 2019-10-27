from django.urls import path

from . import views

urlpatterns = [
    path('', views.application, name='application'),
    path('solicitud/', views.new , name='new'),
    path('pendiente/', views.pendant, name='pendant'),
    path('exitosa/', views.success, name='success'),
]





