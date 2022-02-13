import telegram
from telegram.ext import Updater 
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from bot_features import *

def start(update, context):
	text = getStart()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def weather(update, context):
	text = getLocation() + getDate() + getWeather() + getCommands()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def prayertime(update, context):
	text = getLocation() + getDate() + getPrayerTime() + getCommands()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def allinfo(update, context):
	text = getLocation() + getDate() + getWeather() + getPrayerTime() + getCommands()
	context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def changeLocationTo(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text=setLocation(" ".join(context.args)))

def unknown(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, didn't understand that command.")

def main():
    TOKEN = 'your_own_token'
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    weather_handler = CommandHandler('weather', weather)
    prayertime_handler = CommandHandler('prayertime', prayertime)
    allinfo_handler = CommandHandler('allinfo', allinfo)
    changeLocationTo_handler = CommandHandler('changeLocationTo', changeLocationTo)
    unknown_handler = MessageHandler(Filters.command, unknown)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(prayertime_handler)
    dispatcher.add_handler(allinfo_handler)
    dispatcher.add_handler(changeLocationTo_handler)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()

if __name__ == "__main__":
    main()

			