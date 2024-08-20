from django.urls import include, path
from rest_framework import routers


from .views import TokenURLViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register("tokens", TokenURLViewSet, basename="tokenurl")

urlpatterns = [
    path("", include(router.urls)),
]
