from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet
from modules.models import Module, Lesson
from modules.paginations import ModulePagination, LessonPagination
from modules.serializers import ModuleSerializer, LessonSerializer


class ModuleViewSet(ModelViewSet):
    """Эндпоинт для модели образовательного модуля"""
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()
    pagination_class = ModulePagination


class LessonCreateAPIView(CreateAPIView):
    """Эндпоинт для создания урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """Эндпоинт для изменения урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListAPIView(ListAPIView):
    """Эндпоинт для вывода списка всех уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LessonPagination


class LessonRetrieveAPIView(RetrieveAPIView):
    """Эндпоинт для просмотра одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    """Эндпоинт для удаления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
