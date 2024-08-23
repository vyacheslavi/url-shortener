from django.contrib.auth import logout
from django.shortcuts import redirect, render


def main_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "main/index.html")


def users_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "main/users.html")


def shortener_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    return render(request, "main/url-shortener.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("main")
    return render(request, "auth/register.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("main")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("main")
    return redirect("/api/v1/auth/login")
