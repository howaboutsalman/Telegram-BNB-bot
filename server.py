from telegram import *
from telegram.ext import *
import config as C
import json
from Responses import respons, spot_value

bot = Bot(C.bot_key)
print("Trading bot started...")

def start_command(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="use /spot to see your total balance or tipp the name of the coin you want to see the blance of")

def help_command(update, context):
    bot.send_message(
    chat_id=update.effective_chat.id,
    text= "use /spot to see your total balance or tipp the name of the coin you want to see the blance of")

def spot_command(update, context):
    text = str(update.message.text)
    bot.send_message(
    chat_id=update.effective_chat.id,
    text= "wait a secound pleace!")
    response = respons(text)
    bot.send_message(
    chat_id=update.effective_chat.id,
    text= response)

def handle_message(update, context):
    text = str(update.message.text)
    bot.send_message(
    chat_id=update.effective_chat.id,
    text= "wait a secound pleace!")
    response = spot_value(text)
    bot.send_message(
    chat_id=update.effective_chat.id,
    text= response)

def error(update,context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(C.bot_key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler("start", start_command)
    )
    dispatcher.add_handler(
        CommandHandler("help", help_command)
    )
    dispatcher.add_handler(
        CommandHandler("spot", spot_command)
    )
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()
main()
