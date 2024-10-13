from django.urls import path
from .views import *

urlpatterns = [
    path('', profil, name='profil'),
    path('category/', category, name='category'),
    path('category/category_delete/<int:pk>', category_delete, name='category_delete'),
    path('product/', product, name='product'),
    path('product/<int:pk>', product, name='product'),
    path('product/product_status/<int:pk>', product_status, name='product_status'),
    path('product/product_delete/<int:pk>', product_delete, name='product_delete'),
    path('employee/', employee, name='employee'),
    path('employee/<int:pk>', employee, name='employee'),
    path('table/', table, name='table'),
    path('table/table_delete/<int:pk>', table_delete, name='table_delete'),
    path('contact/', contact, name='contact'),
]