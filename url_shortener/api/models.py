import random
from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class TokenURL(models.Model):
    full_url = models.URLField()
    short_url_token = models.CharField(
        max_length=settings.TOKEN_LENGTH,
        unique=True,
        db_index=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shorted_urls",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    requests_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-created_at",)
        unique_together = (
            "full_url",
            "owner",
        )

    def save(self, *args, **kwargs):
        if not self.short_url_token:
            while True:
                self.short_url_token = "".join(
                    random.choices(
                        settings.CHARACTERS,
                        k=settings.TOKEN_LENGTH,
                    )
                )
                if not TokenURL.objects.filter(
                    short_url_token=self.short_url_token,
                ).exists():
                    break
        super().save(*args, **kwargs)
