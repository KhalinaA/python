import urllib.request
import json
from datetime import datetime

# Функция для формирования ссылки на API
def get_url(city):
    api_key = "c341e34f9b7c327502cde34aa7817c5f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}"
    return url

# Функция для получения данных о погоде и записи логов
def get_weather(city):
    # Формируем ссылку на API
    url = get_url(city)

    # Отправляем запрос на сервер и получаем ответ
    response = urllib.request.urlopen(url)

    # Декодируем ответ в формате JSON
    data = json.loads(response.read())

    # Извлекаем нужную информацию
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    description = data["weather"][0]["description"]

    # Выводим информацию в консоль и записываем логи в файл
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log_text = f"[{current_time}] Запрос погоды в городе: {city}\nТемпература: {temp}°C, {description.capitalize()}\nВлажность воздуха: {humidity}%\nСкорость ветра: {wind_speed} м/с\nАтмосферное давление: {pressure} мм рт. ст.\n"

    print(log_text)

    with open("weather_logs.txt", "a") as f:
        f.write(log_text)

get_weather("Tokyo")
