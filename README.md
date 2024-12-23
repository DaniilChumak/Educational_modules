# Django-приложение "Образовательные модули"

## Описание задачи:

Написать небольшой проект на Django и Django Rest Framework с моделью "Образовательные модули".
В модели есть:

* порядковый номер;
* название модуля;
* описание.

### Задача

При создании проекта необходимо:

1. Реализовать для моделей все методы CRUD
2. Полностью покрыть юнит-тестами все модели, сериализаторы и представления.

## Требуемый стэк технологий:

* Python 3.12;
* Django;
* DRF;
* PostgreSQL;
* Git;
* Swagger;
* Redoc;
* Docker;
* Cors.

## Для тестирования в проекте используется UnitTest, для подсчета покрытия используется Coverage.

1. python manage.py test;
2. coverage run --source'.' manage.py test;
3. coverage report.

## Документация проекта:

"http://127.0.0.1:8000/swagger/"
"http://127.0.0.1:8000/redoc/"

## Для запуска приложения:

1. Скопируйте данный репозиторий на локальный компьютер;
2. Создайте .env файл и заполните по шаблону .env.sample;
2. Выполните команду docker-compose up -d --build в терминале.