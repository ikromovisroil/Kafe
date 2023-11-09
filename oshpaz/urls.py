from django.urls import path
from .views import *

urlpatterns = [
    path('',zakas,name='zakas'),
    path('tayor/<int:pk>', tayor, name='tayor'),

]