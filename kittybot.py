import logging
import os

import requests

from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    level=logging.INFO
)

CAT_URL = 'https://api.thecatapi.com/v1/images/search'


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Я пока только умею показывать красивое и смешное.😸\n'
             'Но скоро еще чему-нибудь научусь 😎\n'
             '*слоновские радостные звуки*\n')


def get_new_image():
    try:
        response = requests.get(CAT_URL).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        dog_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(dog_url).json()

    random_cat = response[0].get('url')
    return random_cat


def new_cat(update, context):
    chat = update.effective_chat
    context.bot.send_photo(
        chat.id,
        get_new_image()
    )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.effective_chat.first_name

    buttons = ReplyKeyboardMarkup(
        [
            ['/newcat'],
        ],
        resize_keyboard=True)

    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}! Посмотри какого котика я тебе нашел.',
        reply_markup=buttons
    )
    context.bot.send_photo(chat.id, get_new_image())


def main():
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
