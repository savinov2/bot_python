import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import logging



TOKEN = '5817538532:AAEjWn_okKQe0C9I5nwsV_pbBYXDE5BdObI'

ADMIN = 1328821049

kb_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(types.InlineKeyboardButton(text="Показать заявки"))

kb_user = types.ReplyKeyboardMarkup(resize_keyboard=True)
kb_user.add(types.InlineKeyboardButton(text="Создать заявку"))

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = u'log/mylog.log')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

# class dialog(StatesGroup):
# 	spam = State()
#   blacklist = State()
#   whitelist = State()

# CREATE TABLE advisement (
#      id SERIAL PRIMARY KEY,
#      state BOOLEAN DEFAULT FALSE,
#      name VARCHAR(50),
#      surname VARCHAR(50),
#      grp VARCHAR(20),
#      course VARCHAR(20)
# );

# # получение объекта курсора
# cursor = conn.cursor()
# # Получаем список всех пользователей
# cursor.execute('SELECT * FROM users')
# all_users = cursor.fetchall()
# cursor.close() # закрываем курсор
# conn.close() # закрываем соединение
    
import psycopg2
def db_connect():
    try:
        # пытаемся подключиться к базе данных
        return psycopg2.connect(dbname='db', user='postgres', password='0000', host='localhost', port=5432)
    except psycopg2.Error as e:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print(f'Cannot establish connection to database: {e}')
        return None


@dp.message_handler(commands=['start'])
async def sart(message: types.Message):
    id = message.from_user.id
    user_full_name = message.from_user.first_name
    
    if message.from_user.id == ADMIN:
        logging.info(f'ADMIN {id=} started {user_full_name=}')
        await message.answer('Добро пожаловать в Админ-Панель! Выберите действие на клавиатуре', reply_markup=kb_admin)
    else: 
        logging.info(f'User {id=} started {user_full_name=}')
        await message.answer((f'Привет, {user_full_name}'),reply_markup=kb_user)
        
@dp.message_handler(text="Показать заявки", user_id=ADMIN)
async def show_applications(message: types.Message):
    try:
        conn = db_connect()
        if conn is None:
            await message.answer("Ошибка подключения к базе данных.")
            return

        # Retrieve all applications from the database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM advisement WHERE state = FALSE")
        applications = cursor.fetchall()
        cursor.close()

        if len(applications) > 0:
            response = "Список заявок:\n"
            for app in applications:
                response += f"ID: {app[0]}, Состояние: {app[1]}, Имя: {app[2]}, Фамилия: {app[3]}, Группа: {app[4]}, Курс: {app[5]}\n"
        else:
            response = "Заявок пока нет."

        await message.answer(response)
    except Exception as e:
        logging.error(f"Error while fetching applications: {str(e)}")
        await message.answer("Произошла ошибка при получении списка заявок.")

    
if __name__ == '__main__':
    executor.start_polling(dp)