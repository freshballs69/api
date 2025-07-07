# Вибираємо базовий образ з Python 3.13
FROM python:3.13-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файли з локальної директорії в контейнер
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект у контейнер
COPY . .

# Відкриваємо порт (припустимо 8000)
EXPOSE 8000

# Команда запуску Sanic
CMD ["sanic", "-H", "0.0.0.0", "-p", "8000", "main:app"]
