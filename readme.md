# Доска объявлений

Разработана backend-часть для сайта объявлений. Бэкенд-часть проекта предполагает реализацию следующего функционала:
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

## Стэк:

<div>
   <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" alt="python" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" alt="django" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" alt="psql" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/djangorest/djangorest-original-wordmark.svg" alt="djangorest" width="40" height="40"/>&nbsp;
   <img src="https://github.com/devicons/devicon/blob/master/icons/pytest/pytest-original-wordmark.svg" alt="pytest" width="40" height="40"/>
</div>

[Файл с настройками](config/settings.py)\
[Процедура сброса пароля (UserResetPasswordView и UserResetPasswordConfirmView)](users/views.py)\
[Тесты](tests)\
[URL-запросы для CRUD отзывов и объявлений](items/urls.py)\

## Getting started:

1. [Описать переменные окружения отсюда](.env-sample)
2. Запуск проекта:\
   `docker compose up --build -d`
При запуске проекта автоматически применяться все миграции, а также [команды из fill.py](users/management/commands/fill.py)
3. Адрес для доступа: \
http://localhost:8000/

## Примеры запросов:
'#' - Применится автоматически \
Для объявления:\
`{
"title": "Стул",
"author": , # при создании текующий пользователь = автор
"price": 200,
"description": "Деревянный",
"created_at": #
}` \
Для комментария:\
`{
"text": "Стул классный",
"author": , # то же самое, что и с объявлением 
"ad": 1,
"created_at": #
}` \
Для регистрации и логина:\
`{
"email": "your_email",
"password": "your_password"
}` \
Для сброса пароля пользователем:\
`{
"email": "your_email"
}` \
Для подтверждения сброса пароля:\
`{
"uid": "6",
"token": "JQhvHYDC",
"new_password": "89321fq"
}` \

email: bla@mail.ru
pass: 111
права: суперпользователь

email: olapopaola@mail.ru
pass: 4104141
права: админ

email: jendoc@inbox.ru
pass: 620414
права: обычный пользователь