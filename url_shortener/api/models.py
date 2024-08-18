from datetime import timezone
import random
import uuid
from django.db import models
from django.contrib.auth.models import User

from url_shortener.url_shortener import settings

# Create your models here.


class URL(models.Model):
    id = models.PrimaryKeyField()
    full_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True, db_index=True, blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shorted_urls",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    requests_count = models.IntegerField(default=0)

    class Meta:
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        if not self.short_url:
            while True:
                self.short_url = "".join(
                    random.choices(
                        settings.CHARACTERS,  # алфавит для генерации короткой ссылки мы будем хранить в файле настроек
                        k=settings.TOKEN_LENGTH,  # длину короткой ссылки тоже
                    )
                )
                if not Tokens.objects.filter(  # проверка на уникальность
                    short_url=self.short_url
                ).exists():
                    break
        super().save(*args, **kwargs)
