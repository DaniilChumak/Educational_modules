from django.contrib import admin

from users.models import User

"""Добавили модель User для отображения в панели администратора"""
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email",)
    list_filter = ("id", "email",)