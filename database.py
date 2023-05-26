import psycopg2
import configparser

def db_connect():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')

        dbname = config.get('Settings', 'DB_NAME')
        user = config.get('Settings', 'DB_USER')
        password = config.get('Settings', 'DB_PASSWORD')
        host = config.get('Settings', 'DB_HOST')
        port = config.get('Settings', 'DB_PORT')
        # Попытка подключения к базе данных
        return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    except psycopg2.Error as e:
        # Если подключение не удалось, выводится сообщение об ошибке
        print(f'Не удалось установить соединение с базой данных: {e}')
        return None
