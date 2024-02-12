# import telebot
#
# bot = telebot.TeleBot('6864834290:AAGNa9IFR4G7igfJhdZj2FYFZsF8Ce3NACI')
#
#
# @bot.message_handler(commands=['start']) #/start
# def start(message):
#     mess = f'Cho tam {message.from_user.first_name}?'
#     bot.send_message(message.chat.id, mess)
#
#
# @bot.message_handler()
# def hi(message):
#     if message.text == 'hi':
#         bot.send_message(message.chat.id, f'hi, how can I help?')
#     elif message.text == 'Hello':
#         bot.send_message(message.chat.id, f'Hello, how can I help?')
#     elif message.text == 'Kyrgyzcha':
#         bot.send_message(message.chat.id, f'Саламатсызбы сизге кандай жардам корсото аламын?')
#     elif message.text == 'Bul bot emne kyla alat?':
#         bot.send_message(message.chat.id, 'Эчтеке кыла албайт! Дагы суроолорунар барбы?')
#     elif message.text == 'Jok':
#         bot.send_message(message.text.id, 'Саламатка барыныз! Башка жолукпайбыз деген ойдомун!')
#


# bot.polling(none_stop=True)