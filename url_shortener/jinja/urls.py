from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views as v


urlpatterns = [
    path("", v.main_view, name="main"),
    path("users/register/", v.register_view, name="register"),
    path("users/logout/", v.logout_view, name="logout"),
    path("users/login/", v.login_view, name="login"),
    path("shortener/", v.shortener_view, name="shortener"),
    path("users/", v.users_view, name="users"),
]
