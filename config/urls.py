from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kafe/', include('kafe.urls')),
    path('afitsan/', include('afitsan.urls')),
    path('oshpaz/', include('oshpaz.urls')),
    path('kassa/', include('kassa.urls')),
    path('', include('users.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)