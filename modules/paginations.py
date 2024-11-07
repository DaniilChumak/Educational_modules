from rest_framework.pagination import PageNumberPagination


"""Настройки пагинации для модели образовательного модуля."""
class ModulePagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


"""Настройки пагинации для модели урока."""
class LessonPagination(PageNumberPagination):

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100
