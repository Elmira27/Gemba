import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler #для команд
from telegram.ext import MessageHandler, Filters # для сообщений
token = '885734453:AAFcxaCIG3jJ_wNT1FqNC5ghvZt9wtyOwIA'
def start (update, context):
  text=update.message.text
  chat_id = update.message.chat_id
  print (f"text: {text}")
  print (f"chat_id: {chat_id}")
  context.bot.send_message (chat_id=chat_id, text="Heeeey")
  custom_keyboard = [['18.04.2019'], ['23.04.2019'], ['30.04.2019'],  ['02.05.2019'], ['07.05.2019'], ['10.05.2019'], ['14.05.2019'], ['16.05.2019'], ['21.05.2019'], ['23.05.2019'], ['28.05.2019']]
  reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
  context.bot.send_message(chat_id=chat_id, 
                 text="Когда Гемба?", 
                 reply_markup=reply_markup)
def help (update, context):
  text=update.message.text
  chat_id = update.message.chat_id
  print (f"text: {text}")
  print (f"chat_id: {chat_id}")
  context.bot.send_message (chat_id=chat_id, text="How can i help you")
def message (update,context):
  text= update.message.text
  chat_id=update.message.chat_id
  if text == '18.04.2019':
    context.bot.send_message(chat_id=chat_id, text ="Dream city 2 оч")
  if text == '23.04.2019':
    context.bot.send_message(chat_id=chat_id, text ="Мангилик 2,3 оч")
  if text == '25.04.2019':
    context.bot.send_message(chat_id=chat_id, text ="Времена года Лето 2 оч блок Е")

  if text == '30.04.2019':
    context.bot.send_message(chat_id=chat_id, text ="Nura Esil 3")
  if text == '02.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="BI City Seoul блок H")
  if text == '07.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Арнау 5")
  if text == '10.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Ray Residence 1 оч")
  if text == '14.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Panorama Park 4 оч")
  if text == '16.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="ADAL")
  if text == '21.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Ботанический")
  if text == '23.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Esil Riverside 1 оч")
  if text == '28.05.2019':
    context.bot.send_message(chat_id=chat_id, text ="Only")
  #else:
      #zcontext.bot.send_message(chat_id=chat_id, text ="Отдыхай, Гембы нет)")
upd= Updater (token, use_context=True)
start_handler=CommandHandler ('start', start)
message_handler= MessageHandler(Filters.text,message)
help_handler=CommandHandler ('help', help)

dispatcher =upd.dispatcher
dispatcher.add_handler (start_handler)
dispatcher.add_handler (help_handler)
dispatcher.add_handler (message_handler)

upd.start_polling () #начать слушать 
upd.idle ()# закрыть по окончанию 