from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(Rol)

@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('rol','nomi','parol','author','get_image',)
    list_filter = ('rol','author',)
    search_fields = ('author','nomi',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "image"