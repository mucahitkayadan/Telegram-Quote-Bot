# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:19:31 2020

@author: mucahitkayadan
"""
import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown
from googletrans import Translator

import wikiquote as wq
import random

from config import BOT_TOKEN
from quote_service import get_quote, get_random_quotes
from inline_service import inlinequery

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Hi!')

def help_command(bot, update):
    """Send a message when the command /help is issued."""
    bot.send_message(chat_id=update.message.chat_id, text="Type 'quote' followed by the name of the person who said the quote. For example, 'quote Ataturk'.")

def textpro(bot, update):
    msg = update.message.text.lower()
    senderName = update.message.from_user.first_name
    chat_type = update.message.chat.type
    chat_id = update.message.chat.id
    logger.info("{}: {}".format(senderName, msg))
    
    if msg.startswith('quote'):
        bot.send_message(chat_id=chat_id, text=get_quote(msg))
        logger.info("Bot: Wikiquote of {}".format(msg))
    elif msg.startswith('daily'):
        bot.send_message(chat_id=chat_id, text=get_random_quotes())
        logger.info("Bot: Wikiquote of {}".format(msg[5:]))
    else:
        if chat_type == "group":
            pass
        else:
            bot.send_message(chat_id=chat_id, text="{}, Invalid command".format(senderName))
            logger.info("Bot: Invalid command")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(InlineQueryHandler(inlinequery))

    dp.add_handler(MessageHandler(Filters.text, textpro))

    updater.start_polling()
    logger.info("Bot Server Started")
    updater.idle()

if __name__ == '__main__':
    main()
