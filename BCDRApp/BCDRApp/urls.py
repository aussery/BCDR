from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BCDR.urls')),
    path('api/', include('BCDR.api_urls')),
]
