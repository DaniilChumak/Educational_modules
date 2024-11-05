from django.urls import path
from rest_framework import routers

from modules.apps import ModulesConfig
from modules.views import (ModuleViewSet, LessonCreateAPIView,
                           LessonDestroyAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateAPIView)

app_name = ModulesConfig.name

urlpatterns = [
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
]

router = routers.SimpleRouter()
router.register("modules", ModuleViewSet)

urlpatterns += router.urls
