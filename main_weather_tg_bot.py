from config import tg_bot_token, open_weather_api_key
from main import GetWeather
import telebot

bot = telebot.TeleBot(tg_bot_token)

@bot.message_handler(commands=['start'])
def main(message):
   bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
   bot.send_message(message.chat.id, 'Введи название города, погоду которого хочешь узнать: ')

@bot.message_handler()
def info_wether(message):
   answer = GetWeather(message.text, open_weather_api_key)
   bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)