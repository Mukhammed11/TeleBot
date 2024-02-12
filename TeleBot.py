# import telebot
#
# bot = telebot.TeleBot('6828441081:AAFIqdOoKsnXFShFSIi2ovO5uU3gMIBiqgw')
#
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     helping = f'Бул боттун жардамын алуу учун ушу тизмедеги сандарды жазып корунуз!\n(1) командасы: Саламдашуу!\n(2) командасы: Жумуш тууралуу'
#     bot.send_message(message.chat.id, helping)
#
# @bot.message_handler()
# def command_num(message):
#     if message.text == '1':
#         bot.send_message(message.chat.id, f'Саламатчылык кош келдиниз?')
#     elif message.text == '2':
#         bot.send_message(message.chat.id, f'Бизде жушуш оордулары бар! Тизмеси учун "+" калдырыныз')
#     elif message.text == '+':
#         bot.send_message(message.chat.id, 'Ооба ! \nA: Официант \nB: Mенеджер \nC: Уктап жатуу ')
#     elif message.text == 'A':
#         bot.send_message(message.chat.id, 'Загрузка...')
#     # elif message.text == 'B':
#     #     bot.send_message(message.chat.id, 'Загрузка...')
#     elif message.text == 'foto':
#         foto = open('media/IMG_1448.jpeg', 'rb')
#         bot.send_photo(message.chat.id, foto)
#     elif message.text == 'audio':
#         audio = open('media/-4546404043149679501.mp4', 'rb')
#         bot.send_audio(message.chat.id, audio)
#     elif message.text == 'video':
#         video = open('media/RPReplay_Final1704455754.mov', 'rd')
#     elif bot.send_video(message.chat.id, video=)













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
#     elif message.text == 'Kyrgyzhcha':
#         bot.send_message(message.chat.id, f'Саламатсызбы сизге кандай жардам корсото аламын?')
#     elif message.text == 'Bul bot emne kyla alat?':
#         bot.send_message(message.chat.id, 'Эчтеке кыла албайт! Дагы суроолорунар барбы?')
#     elif message.text == 'Jok':
#         bot.send_message(message.text.id, 'Саламатка барыныз! Башка жолукпайбыз деген ойдомун!')










# bot.polling(none_stop=True)