# Використовуємо офіційний Python образ як базовий
FROM python:3.11-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо requirements.txt у контейнер
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код з локальної машини в контейнер
COPY . .

# Відкриваємо порт, який буде використовуватись для Flask
EXPOSE 8080

# Вказуємо команду для запуску додатка
CMD ["functions-framework", "--target", "check_number", "--port", "8080"]
