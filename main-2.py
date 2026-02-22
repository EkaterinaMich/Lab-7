import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = os.getenv('api_weather')

class WeatherModel:
    def __init__(self, api=API_KEY, url=WEATHER_URL):
        self.api = api
        self.url = url

    def get_weather(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api,
            'units': 'metric',
            'lang': 'ru'
        }

        try:
            res = requests.get(self.url, params=params)

            # если код ответа не 200 — вызовет исключение
            res.raise_for_status()

            data = res.json()

            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            hum = data['main']['humidity']
            pres = data['main']['pressure']

            return f"""Погода в {city_name}:
Температура: {temp}°C
Описание: {desc}
Влажность: {hum}%
Давление: {pres} гПа"""

        except requests.exceptions.HTTPError:
            return "Ошибка: город не найден или неверный API ключ."

        except requests.exceptions.ConnectionError:
            return "Ошибка подключения к интернету."

        except Exception as e:
            return f"Произошла ошибка: {e}"


if __name__ == '__main__':
    weather = WeatherModel()
    city = 'Moscow'
    result = weather.get_weather(city)
    print(result)