import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler
import kuna.kuna as kuna
import trading_bot.kuna_api_access.kuna_local_config as kuna_config

import trading_bot.bot_local_config as cfg

updater = Updater(token=cfg.BOT_TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#Setup KunaAPI connection
graph_kuna = kuna.KunaAPI(access_key=kuna_config.KUNA_API_PUBLIC_KEY,
                          secret_key=kuna_config.KUNA_SECRET_KEY)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, я бот который поможет тебе торговать на бирже KUNA.IO")

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()