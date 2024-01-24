import os

import psycopg2
from dotenv import load_dotenv
from telebot import types

load_dotenv()

def filter_keyboard(buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in buttons:
        markup.add(el[0])
    return markup

def start_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Показать несколько советов')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Показать пул тренировок')
    btn3 = types.KeyboardButton('Показать упражнения')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn4)
    return markup

def template_hint(hints):
    text = ''
    for el in hints:
        text += f'{el[1]}. {el[2]}\n\n'
    return text

def connect_db(query):
    #'postgresql://user:password@host:port/database_name'
    #try:
        connection = psycopg2.connect(
            #db = os.getenv('DB_ENGINE'),
            dbname = 'postgres',
            user =  os.getenv('POSTGRES_USER'),
            password = os.getenv('POSTGRES_PASSWORD'),
            host = os.getenv('DB_HOST'),
            port = os.getenv('DB_PORT')
        )
        cursor = connection.cursor()

        cursor.execute(query)
        data = cursor.fetchall()

    # except (Exception):
    #     print("Ошибка при работе с PostgreSQL")
    # finally:
        if connection:
            cursor.close()
            connection.close()
            return data

def get_query(query, value):
    return query.replace('CALL', value)
