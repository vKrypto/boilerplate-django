from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('prometheus/', include('django_prometheus.urls')),
    path("admin/", admin.site.urls),
]
