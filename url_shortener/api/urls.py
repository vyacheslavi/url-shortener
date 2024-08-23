from django.urls import include, path
from rest_framework import routers


from .views import TokenURLViewSet, UserTokenListAPIView

app_name = "api"

router = routers.DefaultRouter()
router.register("tokens", TokenURLViewSet, basename="tokenurl")
router.register("users", UserTokenListAPIView, basename="usertokens")

urlpatterns = [
    path("", include(router.urls)),
]
