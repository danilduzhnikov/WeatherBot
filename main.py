from config import open_weather_api_key
import requests


def GetWeather(city, token):
    code_emoji = {
        "Clear": 'Clear \U00002600',
        "Clouds": 'Clouds \U00002601',
        "Rain": 'Rain \U00002614',
        "Drizzle": 'Rain \U00002614',
        "Thunderstorm": 'Thunderstorm \U000026A1',
        "Snow": 'Snow \U0001F328',
        "Mist": 'Mist \U0001F32B'
    }
    try:

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric&lang=ru')
        data = response.json()

        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wid_speed = data['wind']['speed']
        icon_code = data['weather'][0]['main']

        icon = None
        for type in code_emoji:
            if type == icon_code:
                icon = code_emoji[type]

        answer = (f'Город: {city} - {icon}\n'
                  f'Температура: {int(temp)} °C\n'
                  f'Влажность воздуха: {int(humidity)} г/м³\n'
                  f'Скорость ветра: {int(wid_speed)} м/с')
        return answer

    except Exception:
        answer = 'Неверный формат данных'
        return answer

def main_wether():
    city = input('Введите город, погоду которого хотите узнать: ')
    GetWeather(city, open_weather_api_key)

if __name__ == '__main__':
    main_wether()