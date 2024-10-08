from django.contrib import admin

from .models import TokenURL


@admin.register(TokenURL)
class TokenAdmin(admin.ModelAdmin):
    list_display = (
        "full_url",
        "short_url_token",
        "owner",
        "created_at",
        "requests_count",
        "is_active",
    )
    search_fields = ("full_url", "short_url_token")
    ordering = ("-created_at",)
