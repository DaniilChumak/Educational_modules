from django.contrib import admin
from modules.models import Module, Lesson


"""Добавили модель Module для отображения в панели администратора"""
@admin.register(Module)
class EducationModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description",)
    list_filter = ("title",)
    search_fields = ("title",)


"""Добавили модель Lesson для отображения в панели администратора"""
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("number", "title", "module",)
    list_filter = ("number",)
    search_fields = ("title", "module",)