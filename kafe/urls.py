from django.urls import path
from .views import *

urlpatterns = [
    path('', profil, name='profil'),
    path('category/', category, name='category'),
    path('category/<int:pk>', category_delete, name='category_delete'),
    path('product_new/', product_new, name='product_new'),
    path('product/<int:pk>', product, name='product'),
    path('product_delete/<int:pk>', product_delete, name='product_delete'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('stol/', stol, name='stol'),
    path('stol_delete/<int:pk>', stol_delete, name='stol_delete'),
    path('xodim_register/', xodim_register, name='xodim_register'),
    path('xodim_delete/<int:pk>', xodim_delete, name='xodim_delete'),
    path('yordam/', yordam, name='yordam'),
]
