from django.urls import path
from .views import *

urlpatterns = [
    path('tables/', tables, name='tables'),
    path('tables/order/<int:table_pk>/', order, name='order'),
    path('tables/order/<int:table_pk>/<int:category_pk>/', order, name='order'),
    path('tables/order/order_delete/<int:pk>', order_delete, name='order_delete'),
    path('tables/orders/<int:pk>', orders, name='orders'),
    path('tables/orders/order_edit/<int:pk>', order_edit, name='order_edit'),
    path('cook/', cook, name='cook'),
    path('cook/order_status/<int:pk>', order_status, name='order_status'),
    path('report/<int:pk>', report, name='report'),
    path('report/report_delete/<int:pk>', report_delete, name='report_delete'),
]