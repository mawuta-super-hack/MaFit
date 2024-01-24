import os
import pathlib
import webbrowser
from pathlib import Path

import telebot
from dotenv import load_dotenv
from func import (connect_db, filter_keyboard, get_query, start_keyboard,
                  template_hint)
from query import (QUERY_FILTER_EXERCISE, QUERY_FILTER_MUSCLE,
                   QUERY_FILTER_TAGS, QUERY_FILTER_WORKOUTS, QUERY_HINTS,
                   QUERY_RESULT_EXERCISE, QUERY_RESULT_WORKOUTS)
from telebot import types

load_dotenv()


bot=telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))


@bot.callback_query_handler(func=lambda call: True)
def workouts(call):
    workout = call.text
    query = get_query(QUERY_RESULT_WORKOUTS, workout)
    workout = connect_db(query)

    info = ''
    for el in workout:
        path = Path(pathlib.Path.cwd(), 'media', el[0])
        file = open(path, 'rb')
        #file = open(f'/media/{el[0]}', 'rb')
        info += el[1].upper() + '\n' + el[2]
        bot.send_photo(call.chat.id, file)
        bot.send_message(call.chat.id, info)
        info = ''

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add('Вернуться в начало')
    bot.send_message(call.chat.id, 'Удачной тренировки!😎', reply_markup=markup)
    bot.register_next_step_handler(call, start)

@bot.callback_query_handler(func=lambda call: True)
def exercise(call):
    exercise = call.text
    query = get_query(QUERY_RESULT_EXERCISE, exercise)
    exercise = connect_db(query)

    info = ''
    path = Path(pathlib.Path.cwd(), 'media', exercise[0][0])
    file = open(path, 'rb')
    print(path)
    info += exercise[0][1].upper() + '\n' + exercise[0][2]
    bot.send_photo(call.chat.id, file)
    bot.send_message(call.chat.id, info)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add('Вернуться в начало')
    bot.send_message(call.chat.id, 'Есть ли у Вас еще вопросы?', reply_markup=markup)
    bot.register_next_step_handler(call, start)

@bot.callback_query_handler(func=lambda call: True)
def tags_filter(call):
    tag = call.text
    query = get_query(QUERY_FILTER_WORKOUTS, tag)
    buttons = connect_db(query)
    markup = filter_keyboard(buttons)

    info = 'Пожалуйста, выберите какую тренировку показать:'
    bot.send_message(call.chat.id, info, reply_markup=markup)
    bot.register_next_step_handler(call, workouts)


@bot.callback_query_handler(func=lambda call: True)
def muscle_filter(call):
    muscle = call.text
    query = get_query(QUERY_FILTER_EXERCISE, muscle)
    buttons = connect_db(query)
    markup = filter_keyboard(buttons)
        
    info = 'Пожалуйста, выберите упражнение:'
    bot.send_message(call.chat.id, info, reply_markup=markup)
    bot.register_next_step_handler(call, exercise)


@bot.callback_query_handler(func=lambda call: True)
def on_click(call):
    if call.text == 'Показать несколько советов':
        hints = connect_db(QUERY_HINTS)
        text = template_hint(hints)
        bot.send_message(call.chat.id, text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add('Вернуться в начало')
        bot.send_message(call.chat.id, 'Эти ценная информация для новичков!', reply_markup=markup)
        bot.register_next_step_handler(call, start)
        
    elif call.text == 'Показать пул тренировок':
        buttons = connect_db(QUERY_FILTER_TAGS)
        markup=filter_keyboard(buttons)
        
        bot.send_message(call.chat.id, 'Пожалуйста, выберите вид тренировки:', reply_markup=markup)
        bot.register_next_step_handler(call, tags_filter)

    elif call.text == 'Показать упражнения':
        buttons = connect_db(QUERY_FILTER_MUSCLE)
        markup=filter_keyboard(buttons)
        
        bot.send_message(call.chat.id, 'Пожалуйста, веберите группу мышц:', reply_markup=markup)
        bot.register_next_step_handler(call, muscle_filter)

    elif call.text == 'Перейти на сайт':
        webbrowser.open('http://51.250.27.243:8000/')


@bot.message_handler(commands=['start'])
def start(message):
    markup = start_keyboard()

    text = f'{message.from_user.first_name}, чем могу помочь?'
    bot.send_message(message.chat.id, text, reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

# @bot.message_handler()
# def unknown(message):
#     if message.text == '/start' or 'Вернуться в начало':
#         bot.register_next_step_handler(message, start)
        
#     else:
#         text = f'{message.from_user.first_name}, я так не умею)\n'+ 'Пожалуйста, выберите что-то из предложенных опций'
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True).add('..Ой..')
#         bot.send_message(message.chat.id, text, reply_markup=markup)
#         bot.register_next_step_handler(message, start)

bot.polling(none_stop=True)

