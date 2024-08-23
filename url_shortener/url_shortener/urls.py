from api import services
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("api.urls")),
    path("<str:short_url>", services.redirection),
    path("api/v1/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include("jinja.urls")),
]
