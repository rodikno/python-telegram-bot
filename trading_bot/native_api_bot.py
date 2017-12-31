import telebot
from telebot import types
import trading_bot.bot_local_config as cfg
import kuna.kuna as kuna

import trading_bot.kuna_api_access.kuna_local_config as kuna_config

bot = telebot.TeleBot(cfg.BOT_TOKEN)

kuna_api = kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                        secret_key=kuna_config.KUNA_SECRET_KEY)


@bot.message_handler(commands=['Узнать курс'])
def send_some(message):
    bot.send_message(message.chat.id, text='Hello mthfck')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        current_chat_id = call.message.chat.id
        if call.data == 'exchange_rates':
            markup = types.InlineKeyboardMarkup()

            btn_btcuah = types.InlineKeyboardButton(text='BTC/UAH', callback_data='exchange_rate_btcuah')
            btn_ethuah = types.InlineKeyboardButton(text='ETH/UAH', callback_data='exchange_rate_ethuah')
            btn_wavesuah = types.InlineKeyboardButton(text='WAVES/UAH', callback_data='exchange_rate_wavesuah')
            btn_gbguah = types.InlineKeyboardButton(text='GBG/UAH', callback_data='exchange_rate_gbguah')
            btn_kunbtc = types.InlineKeyboardButton(text='KUN/BTC', callback_data='exchange_rate_kunbtc')
            btn_bchbtc = types.InlineKeyboardButton(text='BCH/BTC', callback_data='exchange_rate_bchbtc')

            markup.add(btn_btcuah, btn_ethuah, btn_wavesuah, btn_gbguah, btn_kunbtc, btn_bchbtc)

            bot.send_message(chat_id=call.message.chat.id, text='Please choose a currency pair:', reply_markup=markup)
            return
        if call.data == 'market_data':
            bot.send_message(chat_id=call.message.chat.id, text='Called market data mthfucka')
            return
        if call.data == 'exchange_rate_btcuah':
            market_data = kuna_api.get_recent_market_data('btcuah')
            latest_price = market_data['ticker']['last']
            msg = f"Текущая цена: {latest_price} UAH за один BTC"
            bot.send_message(chat_id=current_chat_id, text=msg)
            return
        if call.data == 'exchange_rate_ethuah':
            market_data = kuna_api.get_recent_market_data('ethuah')
            latest_price = market_data['ticker']['last']
            msg = f"Текущая цена: {latest_price} UAH за один ETH"
            bot.send_message(chat_id=current_chat_id, text=msg)
            return
        if call.data == 'exchange_rate_wavesuah':
            market_data = kuna_api.get_recent_market_data('wavesuah')
            latest_price = market_data['ticker']['last']
            msg = f"Текущая цена: {latest_price} UAH за один WAVES"
            bot.send_message(chat_id=current_chat_id, text=msg)
            return
    # elif call.inline_message_id:
    #     if call.data == 'exchange_rates':
    #         bot.edit_message_text(inline_message_id=call.inline_message_id, text='HUYAK')
    return


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, 'Пожалуйста, выберите одну из доступных команд')


bot.polling()
