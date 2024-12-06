# HackatonTPU: Инструкция по запуску проекта через Docker

## Требования

Для запуска проекта через Docker вам понадобятся:

- Docker версии 20.10 и выше

---

## Установка и запуск проекта

### 1. Клонирование репозитория

Склонируйте репозиторий проекта на ваш локальный компьютер:

```bash
git clone https://github.com/gigastack-official/hackatonTPU.git
cd hackatonTPU
```

---

### 2. Настройка окружения

Создайте файл `.env` в корневой директории проекта и заполните его следующими параметрами:

```env
# Django settings
DEBUG=1
SECRET_KEY =ваш_секретный_ключ
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] hackatonTPU 192.168.0.77

# Database settings
DB_NAME=hacatonTPU
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

> Замените значения на необходимые в вашем окружении.

---

### 3. Сборка Docker-образов

Соберите Docker-образы для всех сервисов:

```bash
docker-compose build
```

---

### 4. Применение миграций

Выполните миграции базы данных для подготовки схемы:

```bash
docker-compose run web python manage.py migrate
```

---

### 5. Создание суперпользователя

Создайте суперпользователя для доступа к административной панели:

```bash
docker-compose run web python manage.py createsuperuser
```

Следуйте инструкциям в консоли, чтобы задать логин, email и пароль.

---

### 6. Сбор статических файлов

Соберите статические файлы для корректной работы фронтенда:

```bash
docker-compose run web python manage.py collectstatic --noinput
```

---

### 7. Запуск приложения

Запустите все сервисы с помощью Docker Compose:

```bash
docker-compose up
```

Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

---


## Дополнительные команды

### Остановка всех сервисов

```bash
docker-compose down
```

### Очистка томов и неиспользуемых контейнеров

```bash
docker-compose down --volumes --remove-orphans
```

### Просмотр логов

```bash
docker-compose logs -f
```

---
