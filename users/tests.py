from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from users.models import User

"""Тестирование эндпоинтов пользователя"""
class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com", password="12345", country="Switzerland"
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    """Тест создания пользователя"""
    def test_user_create(self):
        url = reverse("users:register")
        data = {"email": "test_test@yandex.ru", "password": "54321"}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get("email"), "test_test@yandex.ru")


    """Тест просмотра списка пользователей"""
    def test_user_list(self):
        url = reverse("users:user_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест изменения данных пользователя"""
    def test_user_update(self):
        url = reverse("users:user_update", kwargs={"pk": self.user.id})
        data = {
            "country": "Russia",
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест удаления пользователя"""
    def test_user_delete(self):
        url = reverse("users:user_delete", kwargs={"pk": self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
