# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:19:31 2020

@author: muham
"""
import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram.utils.helpers import escape_markdown

import wikiquote as wq
import random
from googletrans import Translator
# put your toen here

BOT_TOKEN= "1278486866:AAE_UjGv8h3iyQ9CPyozoMv0FJkEQ2EXtgc"
updater= Updater(BOT_TOKEN)  #Bot Token is given by BotFather on Telegram while creating bot. 

def translate(sentence):
    translator = Translator()
    lang = translator.detect(sentence)
    if not lang == "en":
        return translator.translate(sentence,dest='en').text
    else:
        return sentence
    
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Hi!')
    #update.message.reply_text('Hi!')


def help_command(bot, update):
    """Send a message when the command /help is issued."""
    #update.message.reply_text('Help!')
    bot.send_message(chat_id=update.message.chat_id, text="" + 
                     "Type quote and name of person who said this quote. \n i.e quote Ataturk")

def inlinequery(bot, update):
    """Handle the inline query."""
    #query = update.inline_query.query
    query = bot.InlineQuery().query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)




def get_quote(word):
    try:
        search = wq.search(word)[0]
        quote = wq.quotes(search, lang="en")
        unchecked = random.choice(quote)
        final_step = translate(unchecked)
        return final_step
    except:
        return "Quote not found"
def get_random_quotes():
    try:
        return wq.qotd()
    except:
        return "Quote not found"
def textpro(bot, update):
    msg = update.message.text.lower()
    senderName= update.message.from_user.first_name
    chat_type = update.message.chat.type
    chatid= update.message.chat.id
    print("{}: {}".format(senderName, msg))
    if(msg.startswith('quote')):
        bot.send_message(chat_id= chatid,text= get_quote(msg))
        print("Bot: Wikiquote of {}".format(msg))
    elif(msg.startswith('daily')):
        bot.send_message(chat_id= chatid,text= get_random_quotes())
        print("Bot: Wikiquote of {}".format(msg[5:]))
    else:
        if chat_type == "group":
            pass
        else:
            bot.send_message(chat_id= chatid, text= "{}, Invalid command".format(senderName))
            print("Bot: Invalid command")
        
        
#def main():      
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(InlineQueryHandler(inlinequery))
    
updater.dispatcher.add_handler(MessageHandler(Filters.text, textpro))
updater.start_polling()
print("Bot Server Started")
updater.idle()

# if __name__ == '__main__':
#     main()


#DONE