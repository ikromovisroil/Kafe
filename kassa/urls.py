from django.urls import path
from .views import *

urlpatterns = [
    path('',kabina,name='kabina'),
    path('shot/<int:pk>', shot, name='shot'),
    path('tozalash/<int:pk>', tozalash, name='tozalash'),
]