# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.7
FROM python:3.9
# Скопируем файл с зависимостями в контейнер
COPY requirements.txt .
# Установим зависимости внутри контейнера
RUN pip3 install -r requirements.txt
# Скопируем остальные файлы в контейнер
COPY . .
# запускаем скрипт
CMD ["python", "./run_bot.py"]