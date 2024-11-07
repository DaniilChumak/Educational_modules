from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("modules/", include("modules.urls", namespace="modules")),
    path("users/", include("users.urls", namespace="users")),
]
