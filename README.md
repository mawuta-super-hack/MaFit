### Проект MaFit - приложение для любителей фитнеса, где пользователи могут выбирать упражнения из базы данных, объединять их в тренировки и отслеживать свой прогресс.

### Возможности API:

1. Просматривать общие советы по фитнесу, различные упражнения и тренировки добавленные пользователями.
2. Авторизованные пользователи также могут добавлять, редактировать и удалять свои упражнения и тренировки. 
3. Авторизованные пользователи могут добавлять тренировки в избранное. 
4. Также для авторизованных пользователей есть возможность вести историю тренировок: записывать данные о количествах подходов, повторений и используемых весах. 


### Пример наполнения .env-файла:
```
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='db'
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432
SECRET_KEY='<some-key>'
TELEGRAM_TOKEN='<some-token>'
```

### Описание команд для запуска приложения локально:

Клонирование репозитория:

```
git clone https://git@github.com:mawuta-super-hack/MaFit.git
```


Установка и активация виртуального окружения:

```
python -m venv env
```

```
source venv/Scripts/activate
```


Запуск docker-compose:
```
docker-compose up -d --build
```

Выполнение миграций:
```
docker-compose exec web python manage.py migrate
```

Создание суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Cбор статики:
```
docker-compose exec web python manage.py collectstatic --no-input 
```

Создание резервной копии БД:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```


Автор проекта:
<br>
Клименкова Мария [Github](https://github.com/mawuta-super-hack)<br>