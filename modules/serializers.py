from rest_framework import serializers

from modules.models import Module, Lesson

"""Сериализатор для модели урока"""
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"


"""Сериализатор для модели образовательного модуля"""
class ModuleSerializer(serializers.ModelSerializer):
    """Вложенность списка уроков в модуль"""
    lessons = LessonSerializer(many=True, read_only=True, source="lesson_set")

    class Meta:
        model = Module
        fields = "__all__"



