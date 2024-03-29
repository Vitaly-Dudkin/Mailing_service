SkyChimp

SkyChimp - это менеджер рассылок, который помогает клиентам отправлять электронные письма с помощью сторонних сервисов. Кроме того, проект предоставляет возможность регистрации и авторизации пользователей через верификационное письмо, а также просмотр блога, который ведёт контент-менеджер.
Установка и запуск проекта

Для запуска проекта необходимо выполнить следующие шаги:

    Клонировать репозиторий:

git clone git@github.com:swagytor/SkyChimp.git

    Установить зависимости:

pip install -r requirements.txt

    Создать базу данных:

python manage.py migrate

    Запустить локальный сервер:

python manage.py runserver

    Открыть приложение в браузере по адресу http://localhost:8000/

Использование проекта
Регистрация и авторизация

Для регистрации нового пользователя необходимо нажать на кнопку "Регистрация" на главной странице приложения. После заполнения формы регистрации на указанный электронный адрес будет отправлено верификационное письмо. После подтверждения email пользователь сможет авторизоваться на сайте.

У каждого пользователя будет свой собственный набор рассылок и клиентов, так что вы не сможете перейти на чужих клиентов или рассылки
Отправка рассылок

Для отправки рассылки необходимо зарегистрироваться и авторизоваться на сайте, создать рассылочное письмо, добавить клиентов, и после нажать "Создать рассылку".

Здесь нужно указать получателей и текст сообщения, после чего нажать кнопку подтверждения.
Просмотр блога

На главной странице приложения доступен блог, который ведёт контент-менеджер. Здесь можно просмотреть последние статьи и перейти к полному тексту любой из них.
Технологии
SkyChimp написан на языке Python с использованием фреймворка Django. Для верстки страниц использовался HTML, CSS с библиотекой Bootstrap. Для отправки электронных писем использовалась библиотека Django SMTP.