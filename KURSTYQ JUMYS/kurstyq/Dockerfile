# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт
EXPOSE 5000

# Команда для запуска приложения
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
