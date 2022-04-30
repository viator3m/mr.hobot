import requests
from telegram import Bot

token = '5118106733:AAGDRMWqd6AdtHgJdqVTzhYHTDMO-MjqM70'

bot = Bot(token=token)
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 356080680

response = requests.get(URL).json()
random_cat_url = response[0].get('url')
print(random_cat_url)