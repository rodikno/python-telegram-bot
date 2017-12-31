import telebot
from telebot import types

from trading_bot.native_api_bot import bot

@bot.message_handler(commands=['start', 'help'])
def start_handler(bot):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    welcome_message = "Привет!\n" \
                      "Этот бот поможет узнать текущие курсы валют с биржи kuna.io\n" \
                      "Для того чтобы начать работу с ботом, просто выбери опцию:\n"
    # btn_exchange_rates = types.InlineKeyboardButton(text='Узнать курс', callback_data='exchange_rates')
    # btn_latest_market_data = types.InlineKeyboardButton(text='Данные по рынку', callback_data='market_data')
    btn_exchange_rates = types.KeyboardButton(text='Узнать курс')
    btn_latest_market_data = types.KeyboardButton(text='Данные по рынку')

    markup.add(btn_exchange_rates, btn_latest_market_data)
    bot.send_message(message.chat.id, text=welcome_message, reply_markup=markup)