# ДЗ 3 Django

## Задание

Создате сайт для публикации спортивных результатов

1. Создайте и активируйте виртуальное окружение, установите зависимости:

    ```console
    python -m venv venv
    venv\scripts\activate.bat
    pip install -r requirements.txt
    ```

2. Создайте проект и приложение:

    ```console
    django-admin startproject project .
    django-admin startapp sport
    ```

3. Добавьте приложение в `project\settings.py` в список `INSTALLED_APPS`

4. Запустите веб-сервер и проверьте его работу в браузере

    ```console
    django-admin runserver
    ```

5. Создайте в `models.py` модели `Athlete` и `Event` и поля описывающие данные спортсменов и спортивные соревнования по вашему выбору

6. Добавьте связь типа [Many-to-many](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/) между созданными моделями.

7. Добавьте модели в админку

8. Сгенерируйте и выполните скрипт миграции:

    ```console
    python manage.py makemigrations
    python manage.py migrate
    ```

9. Создайте администратора и внесите несколько записей в базу данных через админку

    ```console
    python manage.py createsuperuser
    ```

10. Создайте главную страницу сайта на которой будут отображаться все события и их участники. Если спортсмен участвовал в нескольких соревнованиях — повторите его.

11. Внесите изменения в модульные тесты в `tests.py` так, чтобы они успешно проходили

## Ссылки

* [Django.fun](https://django.fun/)
* [Документация Django](https://docs.djangoproject.com/)
