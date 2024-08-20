from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import TokenURL


class TestAPI(APITestCase):
    url = "/api/v1/tokens/"

    def setUp(self) -> None:
        user = User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            id=2,
            password="test_password",
        )
        self.client.force_login(user)

        TokenURL.objects.create(
            full_url="https://www.ozon.ru/",
            short_url_token="bDyj17",
            owner_id=2,
        )

    def test_token_create(self):
        creation_data = {
            "full_url": "http://url.test.ru",
        }

        response_create = self.client.post(
            self.url,
            data=creation_data,
        )
        result_create = response_create.json()
        print(result_create)
        self.assertEqual(response_create.status_code, 201)
        self.assertEqual(result_create["full_url"], "http://url.test.ru")
        self.assertEqual(len(result_create["short_url_token"]), 6)
        self.assertIsInstance(result_create, dict)


class TestRedirection(TestCase):
    active_url = "/bDyj17"
    deactive_url = "/pzoKT2"

    def setUp(self) -> None:
        User.objects.create_user(
            username="test_user",
            email="test_user@example.com",
            id=1,
        )
        TokenURL.objects.create(
            full_url="https://www.ozon.ru/",
            short_url_token="bDyj17",
            owner_id=1,
        )

        TokenURL.objects.create(
            full_url="https://habr.com/",
            short_url_token="pzoKT2",
            is_active=False,
            owner_id=1,
        )

    def test_redirection(self):
        response = self.client.get(self.active_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "https://www.ozon.ru/")

    def test_response_counter(self):
        self.assertEqual(
            TokenURL.objects.get(short_url_token="bDyj17").requests_count, 0
        )
        self.client.get(self.active_url)
        self.assertEqual(
            TokenURL.objects.get(short_url_token="bDyj17").requests_count, 1
        )
        self.assertEqual(
            TokenURL.objects.get(short_url_token="pzoKT2").requests_count, 0
        )
        self.client.get(self.deactive_url)
        self.assertEqual(
            TokenURL.objects.get(short_url_token="pzoKT2").requests_count, 0
        )

    def test_deactive_url(self):
        response = self.client.get(self.deactive_url)
        self.assertEqual(response.content, b"Token is not active")
