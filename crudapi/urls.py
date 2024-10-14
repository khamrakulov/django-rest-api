from django.contrib import admin
from django.urls import include, path
from .views import welcome

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", welcome, name="welcome"),
]
