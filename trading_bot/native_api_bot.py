import telebot
from telebot import types
import trading_bot.bot_local_config as cfg

bot = telebot.TeleBot(cfg.BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_exchange_rates = types.InlineKeyboardButton(text='Узнать курс', callback_data='exchange_rates')
    btn_latest_market_data = types.InlineKeyboardButton(text='Данные по рынку', callback_data='market_data')

    markup.add(btn_exchange_rates, btn_latest_market_data)
    bot.send_message(message.chat.id, 'Please choose one of the options:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'exchange_rates':
            bot.send_message(chat_id=call.message.chat.id, text='Called Exchange rates mthfck!')
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
