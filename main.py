import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler #для команд
from telegram.ext import MessageHandler, Filters # для сообщений
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds'] 
creds = ServiceAccountCredentials.from_json_keyfile_name('Elmira -d733fc163f9b.json',scope)
client=gspread.authorize (creds)
url='https://docs.google.com/spreadsheets/d/1kUwxMUe5PigOxQsZ9knPM4tlBooskFviX4Hk0UUQ5HA/edit?usp=sharing'
sheet = client.open_by_url(url).sheet1
result = sheet.get_all_records()

token = '885734453:AAFcxaCIG3jJ_wNT1FqNC5ghvZt9wtyOwIA'
def start (update, context):
  text=update.message.text
  chat_id = update.message.chat_id
  print (f"text: {text}")
  print (f"chat_id: {chat_id}")

  custom_keyboard = []
  for obj in result:
    custom_keyboard.append([obj['Date']])
  
  reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True)
  res = context.bot.send_message(chat_id=chat_id, 
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
  print(text)
  for obj in result:
    if text == obj['Date']:
      context.bot.send_message(chat_id=chat_id, text=obj['Name'])
  
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