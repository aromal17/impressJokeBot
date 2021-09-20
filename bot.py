from telegram.ext import *
from decouple import config

API_KEY = config('API_KEY')

print("bot started")

def handle_message(update, context):
    print(update)
    update.message.reply_text(f"Hi and Welcome")    

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    updater.start_polling(1.0)
    updater.idle()