# Dockerfile

# Используем официальный образ Python в качестве базового
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь код проекта в рабочую директорию
COPY . .

# Создаем директорию для статических файлов
RUN mkdir -p /app/staticfiles

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт, который будет использоваться приложением
EXPOSE 8000

# Определяем команду для запуска приложения с использованием Daphne
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "backendApp.asgi:application"]
