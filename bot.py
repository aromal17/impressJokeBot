from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import json
from decouple import config


API_KEY = config('API_KEY')
bot = telegram.Bot(token=API_KEY)

print("bot started")

def sendOptions():
    stupid_button = telegram.KeyboardButton(text="Stupid")
    fat_button = telegram.KeyboardButton(text="Fat")
    dumb_button = telegram.KeyboardButton(text="Dumb")
    custom_keyboard = [[ stupid_button, fat_button, dumb_button ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=708776891, text='Choose an option from the following joke category',reply_markup=reply_markup)
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    if text == 'stupid':
        update.message.reply_text(f"This is a stupid Joke")    
    elif text == 'fat':
        update.message.reply_text(f"This is a fat Joke")
    elif text == 'dumb':
        update.message.reply_text(f"This is a fat Joke")
    elif text == '/start':
        update.message.reply_text(f"Hey {update['message']['chat']['first_name']}. Hope you are doing great!!! \nWelcome to Impress_Jokes_Bot")
    sendOptions()
    

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    sendOptions()
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    updater.start_polling(1.0)
    updater.idle()