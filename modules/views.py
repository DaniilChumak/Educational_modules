from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from modules.models import Module, Lesson
from modules.serializers import ModuleSerializer, LessonSerializer

"""Эндпоинт для модели образовательного модуля"""
class ModuleViewSet(ModelViewSet):

    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


"""Эндпоинт для создания урока"""
class LessonCreateAPIView(CreateAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Эндпоинт для изменения урока"""
class LessonUpdateAPIView(UpdateAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Эндпоинт для вывода списка всех уроков"""
class LessonListAPIView(ListAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Эндпоинт для просмотра одного урока"""
class LessonRetrieveAPIView(RetrieveAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


"""Эндпоинт для удаления урока"""
class LessonDestroyAPIView(DestroyAPIView):

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
