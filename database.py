import psycopg2
import configparser
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

        # Создание таблицы advisement, если она не существует
        cursor = conn.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS advisement (
            id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            state BOOLEAN DEFAULT FALSE,
            name VARCHAR(50),
            surname VARCHAR(50),
            patronymic VARCHAR(50),
            grp VARCHAR(20),
            course VARCHAR(20),
            certificate_form VARCHAR(50),
            phone VARCHAR(20)
        )
        '''
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()

        return conn
    except (psycopg2.Error, configparser.Error) as e:
        # Если подключение или создание таблицы не удалось, выводится сообщение об ошибке
        logging.error(f'Не удалось установить соединение с базой данных: {e}')
        return None
