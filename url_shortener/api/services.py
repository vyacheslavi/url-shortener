from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import F

from .models import TokenURL


def get_full_url(token_url: str) -> str:
    try:
        token = TokenURL.objects.get(short_url_token__exact=token_url)
        if not token.is_active:
            raise KeyError("Token is not active")
    except TokenURL.DoesNotExist:
        raise KeyError("This urls does not exist in the database")
    token.requests_count = F("requests_count") + 1
    token.save()
    return token.full_url


def redirection(request, short_url):
    try:
        full_link = get_full_url(short_url)
        return redirect(full_link)
    except Exception as e:
        return HttpResponse(e.args)
