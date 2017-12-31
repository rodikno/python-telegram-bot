import logging

from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, ConversationHandler

import kuna.kuna as kuna
import trading_bot.kuna_api_access.kuna_local_config as kuna_config

import trading_bot.bot_local_config as cfg

updater = Updater(token=cfg.BOT_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Setup KunaAPI connection
graph_kuna = kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                          secret_key=kuna_config.KUNA_SECRET_KEY)

def start(bot, update):
    logger.info("Bot started")
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    reply_keyboard = [['Get exchange rate', 'Market data']]
    welcome_message = "Привет!\n" \
                      "Этот бот поможет узнать текущие курсы валют с биржи kuna.io\n" \
                      "Для того чтобы начать работу с ботом, просто выбери опцию:\n"

    update.message.reply_text(welcome_message,
                              reply_markup=ReplyKeyboardMarkup(reply_keyboard,
                                                               one_time_keyboard=True,
                                                               resize_keyboard=True))

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()