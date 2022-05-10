import logging
import os

import requests

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler, \
    CallbackQueryHandler, CallbackContext

from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    level=logging.INFO
)

CAT_URL_PHOTO = 'https://api.thecatapi.com/v1/images/search'
CAt_URL_GIF = 'https://api.thecatapi.com/v1/images/search?mime_types=gif'

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('Ещё фото котика!', callback_data='new_cat'),
            InlineKeyboardButton('Ещё гифку котика!', callback_data='gif')
        ],
    ],
    resize_keyboard=True)


def say_hi(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Я пока только умею показывать красивое и смешное.😸\n'
             'Но скоро еще чему-нибудь научусь 😎\n'
             '*слоновские радостные звуки*\n')


def get_new_image(url: str) -> str:
    try:
        response = requests.get(url).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        dog_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(dog_url).json()

    random_cat = response[0].get('url')
    return random_cat


def new_cat(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat

    context.bot.send_photo(
        chat.id,
        get_new_image(CAT_URL_PHOTO),
        reply_markup=BUTTONS
    )


def new_cat_gif(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat

    context.bot.send_animation(
        chat.id,
        get_new_image(CAt_URL_GIF),
        reply_markup=BUTTONS
    )


def wake_up(update: Update, context: CallbackContext) -> None:
    """Приветствует пользователя. Сразу отправляет фото."""
    chat = update.effective_chat
    name = update.effective_chat.first_name

    context.bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}! Посмотри какого котика я тебе нашел.',
    )
    context.bot.send_photo(
        chat.id,
        get_new_image(CAT_URL_PHOTO),
        reply_markup=BUTTONS
    )


def button(update: Update, context: CallbackContext) -> None:
    """Запускает нужную функцию, в зависимости от запроса."""
    query = update.callback_query
    query.answer()
    if query.data == 'new_cat':
        new_cat(update, context)
    if query.data == 'gif':
        new_cat_gif(update, context)


def main() -> None:
    """Основная логика программы."""
    updater = Updater(token=secret_token)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
