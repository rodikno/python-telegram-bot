import telebot
from telebot import types
import trading_bot.bot_local_config as cfg
import kuna.kuna as kuna

import trading_bot.kuna_api_access.kuna_local_config as kuna_config

bot = telebot.TeleBot(cfg.BOT_TOKEN)

kuna_api = kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                        secret_key=kuna_config.KUNA_SECRET_KEY)


# market_data = kuna_api.get_recent_market_data('btcuah')



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_exchange_rates = types.InlineKeyboardButton(text='Узнать курс', callback_data='exchange_rates')
    btn_latest_market_data = types.InlineKeyboardButton(text='Данные по рынку', callback_data='market_data')

    markup.add(btn_exchange_rates, btn_latest_market_data)
    bot.send_message(message.chat.id, text='Please choose one of the options:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'exchange_rates':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

            btn_btcuah  = types.InlineKeyboardButton(text='BTC/UAH', callback_data='exchange_rate_btcuah')
            btn_ethuah = types.InlineKeyboardButton(text='ETH/UAH', callback_data='exchange_rate_ethuah')
            btn_wavesuah = types.InlineKeyboardButton(text='WAVES/UAH', callback_data='exchange_rate_wavesuah')
            btn_gbguah = types.InlineKeyboardButton(text='GBG/UAH', callback_data='exchange_rate_gbguah')
            btn_kunbtc = types.InlineKeyboardButton(text='KUN/BTC', callback_data='exchange_rate_kunbtc')
            btn_bchbtc = types.InlineKeyboardButton(text='BCH/BTC', callback_data='exchange_rate_bchbtc')

            markup.add(btn_btcuah, btn_ethuah, btn_wavesuah, btn_gbguah, btn_kunbtc, btn_bchbtc)

            bot.send_message(chat_id=call.message.chat.id, text='Please choose a currency pair:', reply_markup=markup)
        if call.data == 'market_data':
            bot.send_message(chat_id=call.message.chat.id, text='Called market data mthfucka')
    # elif call.inline_message_id:
    #     if call.data == 'exchange_rates':
    #         bot.edit_message_text(inline_message_id=call.inline_message_id, text='HUYAK')
    return


@bot.message_handler(commands=['test'])
def test_buttons(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
    #                                    one_time_keyboard=True)
    markup = types.InlineKeyboardMarkup()

    btn = types.InlineKeyboardButton(text='Привет', switch_inline_query='/hello')
    btn2 = types.InlineKeyboardButton(text='Привет', url='https://google.com')

    markup.add(btn, btn2)
    bot.send_message(message.chat.id, 'Нажми кнопку и перейди на гугл', reply_markup=markup)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, 'Пожалуйста, выберите одну из доступных команд')


bot.polling()
