from telegram.ext import Updater,CommandHandler
from telegram import ChatAction
from datetime import datetime, timedelta
from pytz import timezone
from time import sleep
import logging,requests,pytz,re,ast

logging.basicConfig(format='%(asctime)s - %(names - &(levelname)s - %(message)s',level=logging.INFO)

updater=Updater(token="YOUR_TOKEN_KEY")
dispatcher=updater.dispatcher

def start(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.2)
    bot.sendMessage(chat_id=update.message.chat_id, text= '''
Hey!! I'm currently Working with ASET ALIAS To hire me contact my admin
Use /help to get help''')

def website(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.2)
    bot.sendMessage(chat_id=update.message.chat_id, text="http://www.asetalias.in")

def facebok(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.2)
    bot.sendMessage(chat_id=update.message.chat_id, text='https://www.facebook.com/asetalias/')

def youtube(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.3)
    bot.sendMessage(chat_id=update.message.chat_id, text="https://www.youtube.com/channel/UCKkyqEMLFW3jz-q3nJIFL3g")

def github(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    sleep(0.3)
    bot.sendMessage(chat_id=update.message.chat_id, text="github.com/asetalias")

def help(bot, update):
     bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
     sleep(0.3)
     bot.sendMessage(chat_id=update.message.chat_id, text='''Use one of the following commands
/mailinglist - to get Aset Alias Mailing List link
/facebook - to get a link to Aset Alias Facebook page
/github - to get a link to Aset Alias Github page
/youtube - to get our youtube channel 

To contribute to|modify me : https://github.com/omi10859/ASET-ALiAS-Bot
''')

dispatcher.add_handler(CommandHandler('start', start))

dispatcher.add_handler(CommandHandler('website', website))
dispatcher.add_handler(CommandHandler('facebook', facebok))
dispatcher.add_handler(CommandHandler('github', github))
dispatcher.add_handler(CommandHandler('youtube', youtube))
dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
