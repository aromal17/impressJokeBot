from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import json
import pandas as pd 
from decouple import config
import psycopg2



API_KEY = config('API_KEY')
DATABASE_URL = config('DB_URL')

bot = telegram.Bot(token=API_KEY)

print("bot started")

def send_options():
    stupid_button = telegram.KeyboardButton(text="Stupid")
    fat_button = telegram.KeyboardButton(text="Fat")
    dumb_button = telegram.KeyboardButton(text="Dumb")
    custom_keyboard = [[ stupid_button, fat_button, dumb_button ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=708776891, text='Choose an option from the following joke category',reply_markup=reply_markup)
    
def update_clicks(new_cnt, joke_type):
    try:
        con = psycopg2.connect(DATABASE_URL)
        cur = con.cursor()
        update_query = """UPDATE clicks SET count = %s WHERE button_name = %s"""
        cur.execute(update_query,(new_cnt, joke_type))
        con.commit()
        print("after") 
        query = f"""SELECT * FROM clicks"""
        results = pd.read_sql(query, con)
        print(results)
        cur.close()
        con.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def get_count(query):
    new_cnt = 0
    try:
        con = psycopg2.connect(DATABASE_URL)
        cur = con.cursor()
        results = pd.read_sql(query, con)
        new_cnt = int(results['count'].values[0]) + 1
        cur.close()
        con.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return new_cnt

def handle_message(update, context):
    joke_type= str(update.message.text).lower()
    print(joke_type)
    if joke_type == 'stupid':
        query = f"""SELECT count FROM clicks WHERE button_name = 'stupid'"""
        new_cnt = get_count(query)
        update_clicks(new_cnt, joke_type)
        update.message.reply_text(f"This is a joke from STUPID category")  
    elif joke_type == 'fat':
        query = f"""SELECT count FROM clicks WHERE button_name = 'fat'"""
        new_cnt = get_count(query)
        update_clicks(new_cnt, joke_type)
        update.message.reply_text(f"This is a joke from FAT category")
    elif joke_type == 'dumb':
        query = f"""SELECT count FROM clicks WHERE button_name = 'dumb'"""
        new_cnt = get_count(query)
        update_clicks(new_cnt, joke_type)
        update.message.reply_text(f"This is a joke from DUMB category")
    elif joke_type == '/start':
        update.message.reply_text(f"Hey {update['message']['chat']['first_name']}. Hope you are doing great!!! \nWelcome to Impress_Jokes_Bot 🚀")
    send_options()
    

if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    send_options()
   
    # con = psycopg2.connect(DATABASE_URL)
    # cur = con.cursor()
    # # joke='stupid'
    # cur.close()
    try:
        con = psycopg2.connect(DATABASE_URL)
        cur = con.cursor()
        # joke_id='stupid'
        # count_no = 10

        query = f"""SELECT * FROM clicks"""
        results = pd.read_sql(query, con)
        print("before")
        print(results)

        # query = f"""SELECT count FROM clicks WHERE button_name = 'stupid'"""
        # results = pd.read_sql(query, con)
        # curr_cnt = int(results['count'].values[0]) + 1
        # update_query = """UPDATE clicks SET count = %s WHERE button_name = %s"""
        # cur.execute(update_query,(curr_cnt, joke_id))
        # con.commit()

        # query = f"""SELECT * FROM clicks"""
        # results = pd.read_sql(query, con)
        # print(results)
        # # cnt = results['count'].values[0]
        # print(curr_cnt)
        cur.close()
        con.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    
    updater.start_polling(1.0)
    updater.idle()