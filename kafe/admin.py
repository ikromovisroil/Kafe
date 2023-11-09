from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nomi','author',)
    list_filter = ('author',)
    search_fields = ('nomi',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','nomi','narxi','author','get_image',)
    list_filter = ('category','author',)
    search_fields = ('nomi',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "image"


@admin.register(Stol)
class StolAdmin(admin.ModelAdmin):
    list_display = ('nomi','author',)
    list_filter = ('author',)
    search_fields = ('nomi',)