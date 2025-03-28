Голосование за лучшего героя 
Этот проект представляет собой веб-приложение для голосования за лучшего героя. 
Пользователи могут добавлять персонажей, голосовать за или против них, 
а также просматривать статистику голосов.

Основные функции

1)Просмотр списка персонажей: 

На главной странице отображается список всех опубликованных персонажей.

2)Детальная информация о персонаже: 

Пользователи могут перейти на страницу персонажа, чтобы увидеть его описание, 
изображение и статистику голосов.

3)Голосование: 

Пользователи могут голосовать за или против персонажа.

4)Добавление, редактирование и удаление персонажей: 

Администраторы могут добавлять новых персонажей, редактировать существующих или 
удалять их.

Технологии
Python: Основной язык программирования.

Django: Веб-фреймворк для создания приложения.

Bootstrap: Используется для стилизации интерфейса.

Pillow: Библиотека для работы с изображениями.

Установка и запуск
1. Клонирование репозитория
Склонируйте репозиторий на ваш компьютер:

git clone https://github.com/yashin-dmitry/vote_hero
cd ваш-репозиторий

2. Создание виртуального окружения
Создайте виртуальное окружение и активируйте его:

python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate     # Для Windows

3. Установка зависимостей
Установите необходимые зависимости:

pip install -r requirements.txt

4. Настройка базы данных
Примените миграции для создания базы данных:

python manage.py migrate

5. Создание суперпользователя
Создайте суперпользователя для доступа к админ-панели:

python manage.py createsuperuser

6. Запуск сервера
Запустите сервер разработки:

python manage.py runserver
Перейдите по адресу http://127.0.0.1:8000/, чтобы увидеть приложение в действии.

Структура проекта
manage.py: Утилита для управления Django-проектом.

models.py: Модели базы данных (например, Character).

views.py: Логика отображения страниц.

urls.py: Маршруты URL.

templates/: HTML-шаблоны для отображения страниц.

static/: Статические файлы (CSS, JS, изображения).

media/: Медиа-файлы (загруженные изображения).


Добавление персонажа:

Перейдите на страницу создания персонажа: http://127.0.0.1:8000/vote/create/.

Заполните форму: имя, описание и загрузите изображение.

Нажмите "Сохранить".

Голосование:

Перейдите на страницу персонажа.

Нажмите "Голосовать за" или "Голосовать против".

Результаты голосования будут отображены на странице.

Админ-панель:

Для управления персонажами через админ-панель перейдите по адресу 
http://127.0.0.1:8000/admin/. Используйте учетные данные суперпользователя 
для входа.