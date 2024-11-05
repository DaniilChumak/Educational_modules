from rest_framework import serializers

from modules.models import Module, Lesson

"""Сериализатор для модели образовательного модуля"""
class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = "__all__"


"""Сериализатор для модели урока"""
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
