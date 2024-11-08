from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from modules.models import Module, Lesson
from modules.serializers import ModuleSerializer, LessonSerializer
from users.models import User


"""Тестирование эндпоинтов образовательного модуля"""
class ModuleTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345",
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.edu_module = Module.objects.create(
            title="test_module",
            description="test_description",
        )


    """Тест создания образовательного модуля"""
    def test_edu_module_create(self):
        data = {
            "title": "some_test_module",
            "description": "some_test_description",
        }
        response = self.client.post("/modules/modules/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Module.objects.all().count(), 2)


    """Тест получения списка всех образовательных модулей"""
    def test_edu_module_get(self):
        response = self.client.get(
            "/modules/modules/",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест изменения данных образовательного модуля."""
    def test_edu_module_patch(self):
        data = {
            "description": "another_test_description",
        }
        response = self.client.patch(
            f"/modules/modules/{self.edu_module.id}/", data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест удаления образовательного модуля"""
    def test_edu_module_delete(self):
        response = self.client.delete(f"/modules/modules/{self.edu_module.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


"""Тестирование эндпоинтов уроков"""
class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test@mail.com",
            password="12345",
        )
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.edu_module = Module.objects.create(
            title="test_module",
            description="test_description",
        )
        self.lesson = Lesson.objects.create(
            module=self.edu_module,
            number=1,
            title="test_lesson",
            description="test_description",
        )


    """Тест создания урока."""
    def test_lesson_create(self):
        url = reverse("modules:lesson_create")
        data = {
            "module": self.edu_module.id,
            "number": "1",
            "title": "some_test_lesson",
            "description": "some_test_description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    """Тест получения списка всех уроков"""
    def test_lesson_list(self):

        url = reverse("modules:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест просмотра одного урока"""
    def test_lesson_retrieve(self):
        url = reverse("modules:lesson_detail", kwargs={"pk": self.lesson.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест изменения данных урока"""
    def test_lesson_update(self):
        url = reverse("modules:lesson_update", kwargs={"pk": self.lesson.id})
        data = {
            "description": "another_test_description",
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    """Тест удаления урока"""
    def test_lesson_delete(self):
        url = reverse("modules:lesson_delete", kwargs={"pk": self.lesson.id})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)


"""Тестирование сериализатора модели - Module"""
class ModuleSerializerTestCase(TestCase):

    def test_edu_module_serializer(self):
        module_1 = Module.objects.create(
            title="test 1", description="test_description_1"
        )
        module_2 = Module.objects.create(
            title="test 2", description="test_description_2"
        )
        data = ModuleSerializer([module_1, module_2], many=True).data
        expected_data = [
            {"id": module_1.id, "title": "test 1", "description": "test_description_1"},
            {"id": module_2.id, "title": "test 2", "description": "test_description_2"}
        ]
        self.assertEqual(data, expected_data)


"""Тестирование сериализатора модели - Lesson"""
class LessonSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.edu_module = Module.objects.create(
            title="test_module",
            description="test_description",
        )

    def test_lesson_serializer(self):
        lesson_data = {
            "module": self.edu_module.id,
            "number": 1,
            "title": "test_lesson",
            "description": "test_description",
        }
        serializer = LessonSerializer(data=lesson_data)
        self.assertTrue(serializer.is_valid())
        lesson = serializer.save()
        self.assertEqual(lesson.module, self.edu_module)
        self.assertEqual(lesson.number, 1)
        self.assertEqual(lesson.title, "test_lesson")
        self.assertEqual(lesson.description, "test_description")