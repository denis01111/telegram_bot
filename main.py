from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


TOKEN = '1073789111:AAE9bFDkI-cdTFvw27FfhalX7mE2-GAh2Ns'


def start(update, context):
    update.message.reply_text('asdad')


def help(update, context):
    update.message.reply_text('123')


def main():
    updater = Updater(TOKEN, use_context=True)
    text_handler = MessageHandler(Filters.text, echo)
    dp = updater.dispatcher
    dp.add_handler(text_handler)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()