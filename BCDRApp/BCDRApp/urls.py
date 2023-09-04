from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BCDR.urls')),  # include the BCDR/urls.py file here
]
