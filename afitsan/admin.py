from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Zakas)
class ZakasAdmin(admin.ModelAdmin):
    list_display = ('product','stol','soni','author','buyurtma',)
    list_filter = ('author',)
    search_fields = ('author',)