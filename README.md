# Бот Python

Это простой бот на Python, который предоставляет различные функции для управления чатами и обработки сообщений.

## Функциональность

- Отправка и получение сообщений в режиме реального времени
- Обработка команд и реакция на них
- Подключение к базе данных PostgreSQL
- Создание и управление таблицами в базе данных
- Логирование действий и ошибок

## Установка

1. Клонируйте репозиторий:

   ```shell
   git clone https://github.com/your-username/your-repo.git
   
2.Создайте файл config.ini и заполните его данными:

   ```shell
      [Settings]
      TOKEN=your-token
      ADMIN=your-admin-id
      DB_NAME=your-db-name
      DB_USER=your-db-user
      DB_PASSWORD=your-db-password
      DB_HOST=your-db-host
      DB_PORT=your-db-port

   
3.Запустите бот:

   ```shell
   python main.py
