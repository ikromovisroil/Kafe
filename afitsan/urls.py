from django.urls import path
from .views import *

urlpatterns = [
    path('',stollar,name='stollar'),
    path('buyurtma/<int:pk>', buyurtma, name='buyurtma'),
    path('buyurtmalar/<int:pk>', buyurtmalar, name='buyurtmalar'),
    path('buyurtmalar_delete/<int:pk>', buyurtmalar_delete, name='buyurtmalar_delete'),
]