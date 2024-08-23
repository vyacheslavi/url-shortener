from django.contrib.auth.models import User
from rest_framework import serializers, status


from .models import TokenURL


class TokenURLSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TokenURL
        fields = ["full_url", "short_url_token", "owner"]

    def create(self, validated_data):
        token, created = TokenURL.objects.get_or_create(**validated_data)
        if created:
            status_code = status.HTTP_201_CREATED
        else:
            status_code = status.HTTP_200_OK
        return token, status_code


class UserTokenSerializer(serializers.ModelSerializer):
    shorted_urls = TokenURLSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "shorted_urls",
        ]
