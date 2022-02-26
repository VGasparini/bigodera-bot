import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from inspect import getmembers, isfunction

import resources
import non_command

def error(update, context):
    update.message.reply_text('Update "%s" caused error "%s"', update, error)

def main():
    TOKEN = os.environ["TELEGRAM_TOKEN"]
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    for trigger,command in getmembers(resources, isfunction):
        dispatcher.add_handler(CommandHandler(trigger,command))

    dispatcher.add_handler(MessageHandler(Filters.text, non_command.noncommand))

    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
