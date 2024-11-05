from django.urls import path
from rest_framework import routers

from modules.apps import ModulesConfig
from modules.views import (ModuleViewSet, LessonCreateAPIView,
                           LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = ModulesConfig.name

urlpatterns = [
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"), #Создание урока
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"), #Просмотр списка уроков
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"), #Просмотр определенного урока
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"), #Редактирование урока
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"), #Удаление урока
]

router = routers.SimpleRouter()
router.register("modules", ModuleViewSet)

urlpatterns += router.urls
